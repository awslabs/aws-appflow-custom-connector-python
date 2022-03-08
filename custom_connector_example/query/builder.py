from typing import List

from custom_connector_sdk.connector.fields import FieldDataType
from custom_connector_sdk.connector.context import EntityDefinition
from custom_connector_queryfilter.queryfilter.parse_tree_builder import parse
from custom_connector_example.query.visitor import SalesforceQueryFilterExpressionVisitor

CONDITION_FORMAT = '{} {} {}'
WHERE_AND = ' and '
CLAUSE_STRING_FORMAT = '{} {}'
WHERE_CLAUSE = 'where'
FROM_CLAUSE = 'from'
SELECT_CLAUSE = 'select'

class QueryObject:
    """Stores parameters to be built into a Salesforce query."""
    def __init__(self,
                 s_object: str,
                 selected_field_names: List[str] = None,
                 filter_expression: str = None,
                 id_field_name: str = None,
                 fields: List[str] = None,
                 data_type: List[str] = None,
                 entity_definition: EntityDefinition = None):
        self.s_object = s_object
        self.selected_field_names = selected_field_names
        self.filter_expression = filter_expression
        self.id_field_name = id_field_name
        self.fields = fields
        self.data_type = data_type
        self.entity_definition = entity_definition

def build_query(query_object: QueryObject) -> str:
    """Build Salesforce specific query given a QueryObject."""
    if not query_object.selected_field_names:
        raise ValueError('No fields were selected for Salesforce Query')

    clauses = []
    conditions = []

    select_fields = ', '.join(query_object.selected_field_names)
    clauses.append(CLAUSE_STRING_FORMAT.format(SELECT_CLAUSE, select_fields))
    clauses.append(CLAUSE_STRING_FORMAT.format(FROM_CLAUSE, query_object.s_object))

    # QueryData allows data filtering based on filter expression.
    if query_object.filter_expression:
        where_clause = translate_filter_expression(query_object.filter_expression, query_object.entity_definition)
        if where_clause:
            clauses.append(CLAUSE_STRING_FORMAT.format(WHERE_CLAUSE, where_clause))
    # RetrieveData allows data filtering based on entity primary ID fields
    elif query_object.id_field_name and query_object.fields and query_object.data_type:
        conditions = add_or_conditions('=',
                                       conditions,
                                       query_object.id_field_name,
                                       query_object.fields,
                                       query_object.data_type)
        if conditions:
            where_clause = WHERE_AND.join(conditions)
            clauses.append(CLAUSE_STRING_FORMAT.format(WHERE_CLAUSE, where_clause))

    return ' '.join(clauses)

def add_or_conditions(operator: str,
                      conditions: List[str],
                      variable: str,
                      values: List[str],
                      value_type: str) -> List[str]:
    """Joins clauses with 'or'"""
    or_conditions = []
    for value in values:
        add_condition(operator, or_conditions, variable, value, value_type)

    condition = '(' + ' or '.join(or_conditions) + ')'
    conditions.append(condition)
    return conditions

def add_condition(operator: str,
                  conditions: List[str],
                  field_name: str,
                  value: str,
                  value_type: str) -> str:
    """Builds an individual condition."""
    value = format_quotes(value_type, value)
    conditions.append(CONDITION_FORMAT.format(field_name, operator, value))
    return conditions

def format_quotes(value_type: str, value: str) -> str:
    """Escapes customer-added quotes, and changes/adds outer quotes as single quotes."""
    customer_quoted = False

    if (value.startswith("'") and value.endswith("'")) or (value.startswith('"') and value.endswith('"')):
        value = value[1:-1]
        customer_quoted = True

    value.replace("'", "\\'")

    if value_type == FieldDataType.Struct.name or customer_quoted:
        return "'" + value + "'"
    return value

def translate_filter_expression(filter_expression: str, entity_definition: EntityDefinition) -> str:
    """Converts filter expression to Salesforce specific expression using FilterExpressionVisitor."""
    if filter_expression:
        parse_tree = parse(filter_expression)
        filter_expression_visitor = SalesforceQueryFilterExpressionVisitor(entity_definition)
        filter_expression_visitor.visit(parse_tree)
        return filter_expression_visitor.get_result()
    return ''
