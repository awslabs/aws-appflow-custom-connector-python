import dateutil.parser
import datetime
from io import StringIO
from typing import Optional, Tuple
from custom_connector_queryfilter.queryfilter.antlr.CustomConnectorQueryFilterParserVisitor import CustomConnectorQueryFilterParserVisitor
from custom_connector_queryfilter.queryfilter.antlr.CustomConnectorQueryFilterParser import CustomConnectorQueryFilterParser
from custom_connector_sdk.connector.context import EntityDefinition
from custom_connector_sdk.connector.fields import FieldDefinition

SPACE = ' '
DATE_TIME = 'DateTime'
DATE = 'Date'
STRING_TYPES = ('String', 'id', 'textarea')
NON_STRING_TYPES = ('Boolean', 'Double', 'double', 'Integer', 'Float', 'Short', 'Long', 'Currency')

CONTAINS = 'CONTAINS'
CONDITION_FORMAT = '{} {} {}'
LIKE = 'LIKE'
LOGICAL_AND = ' and '
COMPARISON_LESSER = '<'
COMPARISON_GREATER = '>'
IN = 'IN'
LEFT_PARENTHESIS = '('
RIGHT_PARENTHESIS = ')'


def salesforce_datetime_format(date_time: datetime.datetime):
    date_time_string = date_time.strftime('%Y-%m-%dT%H:%M:%S')

    # Salesforce only supports milliseconds so microseconds must be truncated
    date_time_string += date_time.strftime('.%f')[:-3]

    date_time_string += date_time.strftime('%z')

    return date_time_string


def format_value(value: str, data_type: str, operator: Optional[str]) -> str:
    has_custom_quotes = len(value) >= 2 and ((value.startswith("'") and value.endswith("'")) or
                                             (value.startswith('"') and value.endswith('"')))
    if has_custom_quotes:
        value = value[1:-1]

    value = value.replace("'", "\\'")

    if data_type == DATE:
        value = dateutil.parser.parse(value).strftime('%Y-%m-%d')
    elif data_type == DATE_TIME:
        value = salesforce_datetime_format(dateutil.parser.parse(value))

    elif data_type in STRING_TYPES or (has_custom_quotes and data_type not in NON_STRING_TYPES):
        # Add wildcards (if applicable) and single quotes
        value = f"'%{value}%'" if operator and operator.upper() == CONTAINS and '%' not in value else f"'{value}'"

    return value


class SalesforceQueryFilterExpressionVisitor(CustomConnectorQueryFilterParserVisitor):
    """This class is responsible for converting filter expression into Salesforce specific filter query. Filter
    expression is passed in as instance of an Antlr parse tree, and this class visits all nodes to form Salesforce
    specific where clause of query.

    """
    def __init__(self, entity_definition: EntityDefinition):
        assert entity_definition, "entity definition can't be null, as it is required for building filter query"
        self.entity_definition = entity_definition
        self.query_builder = StringIO()
        self.limit_builder = StringIO()

    def visitBetweenExpression(self, ctx: CustomConnectorQueryFilterParser.BetweenExpressionContext):
        if ctx.getChildCount() == 5:
            identifier = ctx.getChild(0).getText()
            lower_bound = ctx.getChild(2).getText()
            upper_bound = ctx.getChild(4).getText()
            data_type = self.get_field_data_type(ctx.getChild(0).getText()).data_type.name

            lower_bound_comparison = CONDITION_FORMAT.format(identifier,
                                                             COMPARISON_GREATER,
                                                             format_value(lower_bound, data_type, COMPARISON_GREATER))
            upper_bound_comparison = CONDITION_FORMAT.format(identifier,
                                                             COMPARISON_LESSER,
                                                             format_value(upper_bound, data_type, COMPARISON_LESSER))
            self.query_builder.write(lower_bound_comparison + LOGICAL_AND + upper_bound_comparison + SPACE)
            return self.query_builder.getvalue()

        return self.visitChildren(ctx)

    def visitInExpression(self, ctx: CustomConnectorQueryFilterParser.InExpressionContext):
        if len(ctx.value()) > 0:
            identifier = ctx.getChild(0).getText()
            data_type = self.get_field_data_type(identifier).data_type.name
            values = ','.join([format_value(value.getText(), data_type, None) for value in ctx.value()])
            self.query_builder.write(identifier + SPACE + IN + SPACE + LEFT_PARENTHESIS + values + RIGHT_PARENTHESIS + SPACE)
            return self.query_builder.getvalue()
        return self.visitChildren(ctx)

    def visitGreaterThanEqualToComparatorExpression(self, ctx: CustomConnectorQueryFilterParser
                                                    .GreaterThanEqualToComparatorExpressionContext):
        if ctx.getChildCount() == 1:
            self.query_builder.write(ctx.getText() + SPACE)
            return self.query_builder.getvalue()
        return self.visitChildren(ctx)

    def visitGtComparator(self, ctx: CustomConnectorQueryFilterParser.GtComparatorContext):
        if ctx.getChildCount() == 1:
            self.query_builder.write(ctx.getText() + SPACE)
            return self.query_builder.getvalue()
        return self.visitChildren(ctx)

    def visitGeComparator(self, ctx: CustomConnectorQueryFilterParser.GeComparatorContext):
        if ctx.getChildCount() == 1:
            self.query_builder.write(ctx.getText() + SPACE)
            return self.query_builder.getvalue()
        return self.visitChildren(ctx)

    def visitLtComparator(self, ctx: CustomConnectorQueryFilterParser.LtComparatorContext):
        if ctx.getChildCount() == 1:
            self.query_builder.write(ctx.getText() + SPACE)
            return self.query_builder.getvalue()
        return self.visitChildren(ctx)

    def visitLeComparator(self, ctx: CustomConnectorQueryFilterParser.LeComparatorContext):
        if ctx.getChildCount() == 1:
            self.query_builder.write(ctx.getText() + SPACE)
            return self.query_builder.getvalue()
        return self.visitChildren(ctx)

    def visitEqComparator(self, ctx: CustomConnectorQueryFilterParser.EqComparatorContext):
        if ctx.getChildCount() == 1:
            self.query_builder.write(ctx.getText() + SPACE)
            return self.query_builder.getvalue()
        return self.visitChildren(ctx)

    def visitNeComparator(self, ctx: CustomConnectorQueryFilterParser.NeComparatorContext):
        if ctx.getChildCount() == 1:
            self.query_builder.write(ctx.getText() + SPACE)
            return self.query_builder.getvalue()
        return self.visitChildren(ctx)

    def visitLikeComparator(self, ctx: CustomConnectorQueryFilterParser.LikeComparatorContext):
        if ctx.getChildCount() == 1:
            self.query_builder.write(LIKE + SPACE)
            return self.query_builder.getvalue()
        return self.visitChildren(ctx)

    def visitBetweenComparator(self, ctx: CustomConnectorQueryFilterParser.BetweenComparatorContext):
        if ctx.getChildCount() == 1:
            self.query_builder.write(ctx.getText() + SPACE)
            return self.query_builder.getvalue()
        return self.visitChildren(ctx)

    def visitAndBinary(self, ctx: CustomConnectorQueryFilterParser.AndBinaryContext):
        if ctx.getChildCount() == 1:
            self.query_builder.write(ctx.getText() + SPACE)
            return self.query_builder.getvalue()
        return self.visitChildren(ctx)

    def visitOrBinary(self, ctx: CustomConnectorQueryFilterParser.OrBinaryContext):
        if ctx.getChildCount() == 1:
            self.query_builder.write(ctx.getText() + SPACE)
            return self.query_builder.getvalue()
        return self.visitChildren(ctx)

    def visitIdentifier(self, ctx: CustomConnectorQueryFilterParser.IdentifierContext):
        if ctx.getChildCount() == 1:
            self.query_builder.write(ctx.getText() + SPACE)
            return self.query_builder.getvalue()
        return self.visitChildren(ctx)

    def visitStringValueExpression(self, ctx: CustomConnectorQueryFilterParser.StringValueExpressionContext):
        if ctx.getChildCount() == 1:
            data_type = self.get_field_data_type(ctx.parentCtx.getChild(0).getText()).data_type.name
            value = format_value(ctx.getText(), data_type, ctx.parentCtx.getChild(1).getText())
            self.query_builder.write(value + SPACE)
            return self.query_builder.getvalue()
        return self.visitChildren(ctx)

    def visitDecimalValueExpression(self, ctx: CustomConnectorQueryFilterParser.DecimalValueExpressionContext):
        if ctx.getChildCount() == 1:
            data_type = self.get_field_data_type(ctx.parentCtx.getChild(0).getText()).data_type.name
            value = format_value(ctx.getText(), data_type, ctx.parentCtx.getChild(1).getText())
            self.query_builder.write(value + SPACE)
            return self.query_builder.getvalue()
        return self.visitChildren(ctx)

    def visitIsoDate(self, ctx: CustomConnectorQueryFilterParser.IsoDateContext):
        self.query_builder.write(ctx.getText() + SPACE)
        return self.visitChildren(ctx)

    def visitIsoDateTime(self, ctx: CustomConnectorQueryFilterParser.IsoDateTimeContext):
        self.query_builder.write(salesforce_datetime_format(dateutil.parser.parse(ctx.getText())) + SPACE)
        return self.visitChildren(ctx)

    def visitCountValueExpression(self, ctx:CustomConnectorQueryFilterParser.CountValueExpressionContext):
        self.limit_builder.write(ctx.getText() + SPACE)
        return self.visitChildren(ctx)

    def get_result(self) -> Tuple[str, str]:
        """Returns the final query expression built for Salesforce."""
        return self.query_builder.getvalue().rstrip(), self.limit_builder.getvalue().rstrip()

    def get_field_data_type(self, field_name: str) -> FieldDefinition:
        """Find FieldDefinition for given field name. This definition contains datatype supported by field and other
        useful metadata information required to build filter clause.

        """
        try:
            return next(filter(lambda x: x.field_name == field_name, self.entity_definition.fields))
        except StopIteration:
            raise ValueError('Filter attribute not found in entity definition')
