import custom_connector_sdk.connector.context as context
import custom_connector_sdk.connector.fields as fields
import custom_connector_queryfilter.queryfilter.parse_tree_builder as parse_tree_builder
import custom_connector_queryfilter.queryfilter.errors as errors
from custom_connector_example.query.visitor import SalesforceQueryFilterExpressionVisitor
import unittest

CREATED_DATE = 'CreatedDate'
UPDATED_DATE = 'UpdatedDate'
ACCOUNT_NUMBER = 'AccountNumber'
ID = 'Id'
NAME = 'Name'


class SalesforceQueryFilterExpressionVisitorTest(unittest.TestCase):
    """Test class to validate Salesforce queries built by SalesforceQueryFilterExpressionVisitor."""
    def _test_conversion_from_filter_expression_to_salesforce_query(self,
                                                                    filter_expression: str,
                                                                    expected_where_clause: str,
                                                                    expected_limit_clause: str):
        entity = context.Entity(entity_identifier='Account',
                                has_nested_entities=False,
                                is_writable=False)
        field_definitions = [fields.FieldDefinition(field_name=CREATED_DATE,
                                                    data_type=fields.FieldDataType.DateTime,
                                                    data_type_label='DateTime'),
                             fields.FieldDefinition(field_name=UPDATED_DATE,
                                                    data_type=fields.FieldDataType.Date,
                                                    data_type_label='Date'),
                             fields.FieldDefinition(field_name=NAME,
                                                    data_type=fields.FieldDataType.String,
                                                    data_type_label='String'),
                             fields.FieldDefinition(field_name=ID,
                                                    data_type=fields.FieldDataType.String,
                                                    data_type_label='String'),
                             fields.FieldDefinition(field_name=ACCOUNT_NUMBER,
                                                    data_type=fields.FieldDataType.Long,
                                                    data_type_label='Long')]
        entity_definition = context.EntityDefinition(entity=entity, fields=field_definitions)
        salesforce_query_expression_visitor = SalesforceQueryFilterExpressionVisitor(entity_definition)

        salesforce_query_expression_visitor.visit(parse_tree_builder.parse(filter_expression))
        where_clause, limit_clause = salesforce_query_expression_visitor.get_result()
        self.assertEqual(expected_where_clause, where_clause)
        self.assertEqual(expected_limit_clause, limit_clause)

    def test_query(self):
        expressions = [
            ('Name = "TestAccountName"', 'Name = \'TestAccountName\'', ''),
            ('Id != \'0016g00001cyrfiAAA\' AND AccountNumber = 40',
             'Id != \'0016g00001cyrfiAAA\' AND AccountNumber = 40',
             ''),
            ('limit 100', '', '100'),
            ('CreatedDate > 2021-04-20T10:30:35Z AND AccountNumber = 40',
             'CreatedDate > 2021-04-20T10:30:35.000+0000 AND AccountNumber = 40',
             ''),
            ('CreatedDate between 2021-04-20T10:30:35Z and 2021-04-25T10:30:35Z',
             'CreatedDate > 2021-04-20T10:30:35.000+0000 and CreatedDate < 2021-04-25T10:30:35.000+0000',
             ''),
            ('(AccountNumber > 100 and ((CreatedDate < 2021-04-20T12:30:45Z and CreatedDate > '
             '2021-04-21T15:45:49.234Z) and Name contains \"TestAccountName\"))',
             'AccountNumber > 100 and CreatedDate < 2021-04-20T12:30:45.000+0000 and CreatedDate > '
             '2021-04-21T15:45:49.234+0000 and Name LIKE \'%TestAccountName%\'',
             ''),
            ('(AccountNumber >= 100 and ((CreatedDate <= 2021-04-20T12:30:45Z and CreatedDate >= '
             '2021-04-21T15:45:49.234Z) and Name contains \"TestAccountName\"))',
             'AccountNumber >= 100 and CreatedDate <= 2021-04-20T12:30:45.000+0000 and CreatedDate >= '
             '2021-04-21T15:45:49.234+0000 and Name LIKE \'%TestAccountName%\'',
             ''),
            ('Date = 2018-05-03 OR Date = 2018-04-20', 'Date = 2018-05-03 OR Date = 2018-04-20', ''),
            ('AccountNumber between 1 AND 10', 'AccountNumber > 1 and AccountNumber < 10', ''),
            ('AccountNumber = 1 or (UpdatedDate between 2020-03-05 and 2020-03-07)',
             'AccountNumber = 1 or UpdatedDate > 2020-03-05 and UpdatedDate < 2020-03-07',
             ''),
            ('AccountNumber = 1 or (UpdatedDate between 2020-03-05 and 2020-03-07) limit 100',
             'AccountNumber = 1 or UpdatedDate > 2020-03-05 and UpdatedDate < 2020-03-07',
             '100'),
            ('AccountNumber in (3, 5, 9)', "AccountNumber IN (3,5,9)", '')
        ]
        for filter_expression, expected_where, expected_limit in expressions:
            with self.subTest(expression=filter_expression):
                self._test_conversion_from_filter_expression_to_salesforce_query(filter_expression,
                                                                                 expected_where,
                                                                                 expected_limit)

    def test_invalid_filter_expressions(self):
        expressions = [
            ('AccountNumber BETWEEN 5', errors.InvalidFilterExpressionError),
            ('LIMIT 100 LIMIT 5', errors.InvalidFilterExpressionError),
            ('NotAField = 10', ValueError)
        ]
        for filter_expression, error in expressions:
            with self.subTest(expression=filter_expression, expected_error=error):
                self.assertRaises(error,
                                  self._test_conversion_from_filter_expression_to_salesforce_query,
                                  filter_expression,
                                  '',
                                  '')
