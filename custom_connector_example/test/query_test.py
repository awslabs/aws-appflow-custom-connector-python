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
                                                                    expected_salesforce_query_expression: str):
        entity = context.Entity(entity_identifier='Account',
                                has_nested_entities=False)
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
        self.assertEqual(expected_salesforce_query_expression, salesforce_query_expression_visitor.get_result())

    def test_1(self):
        filter_expression = 'Name = "TestAccountName"'
        expected_salesforce_query_expression = 'Name = \'TestAccountName\' '
        self._test_conversion_from_filter_expression_to_salesforce_query(filter_expression,
                                                                         expected_salesforce_query_expression)

    def test_2(self):
        filter_expression = 'Id != \'0016g00001cyrfiAAA\' AND AccountNumber = 40'
        expected_salesforce_query_expression = 'Id != \'0016g00001cyrfiAAA\' AND AccountNumber = 40 '
        self._test_conversion_from_filter_expression_to_salesforce_query(filter_expression,
                                                                         expected_salesforce_query_expression)

    def test_3(self):
        filter_expression = 'CreatedDate > 2021-04-20T10:30:35Z AND AccountNumber = 40'
        expected_salesforce_query_expression = 'CreatedDate > 2021-04-20T10:30:35.000+0000AND AccountNumber = 40 '
        self._test_conversion_from_filter_expression_to_salesforce_query(filter_expression,
                                                                         expected_salesforce_query_expression)

    def test_4(self):
        filter_expression = 'CreatedDate between 2021-04-20T10:30:35Z and 2021-04-25T10:30:35Z'
        expected_salesforce_query_expression = 'CreatedDate > 2021-04-20T10:30:35.000+0000 and ' +\
                                               'CreatedDate < 2021-04-25T10:30:35.000+0000'
        self._test_conversion_from_filter_expression_to_salesforce_query(filter_expression,
                                                                         expected_salesforce_query_expression)

    def test_5(self):
        filter_expression = '(AccountNumber > 100 and ((CreatedDate < 2021-04-20T12:30:45Z and ' +\
                            'CreatedDate > 2021-04-21T15:45:49.234Z) and Name contains \"TestAccountName\"))'
        expected_salesforce_query_expression = 'AccountNumber > 100 and CreatedDate < 2021-04-20T12:30:45.000+0000' +\
                                               'and CreatedDate > 2021-04-21T15:45:49.234+0000and Name ' +\
                                               'LIKE \'%TestAccountName%\' '
        self._test_conversion_from_filter_expression_to_salesforce_query(filter_expression,
                                                                         expected_salesforce_query_expression)

    def test_6(self):
        filter_expression = '(AccountNumber >= 100 and ((CreatedDate <= 2021-04-20T12:30:45Z and ' +\
                            'CreatedDate >= 2021-04-21T15:45:49.234Z) and Name contains \"TestAccountName\"))'
        expected_salesforce_query_expression = 'AccountNumber >= 100 and CreatedDate <= 2021-04-20T12:30:45.000+0000' +\
                                               'and CreatedDate >= 2021-04-21T15:45:49.234+0000and ' +\
                                               'Name LIKE \'%TestAccountName%\' '
        self._test_conversion_from_filter_expression_to_salesforce_query(filter_expression,
                                                                         expected_salesforce_query_expression)

    def test_7(self):
        filter_expression = 'Date = 2018-05-03 OR Date = 2018-04-20'
        expected_salesforce_query_expression = 'Date = 2018-05-03OR Date = 2018-04-20'
        self._test_conversion_from_filter_expression_to_salesforce_query(filter_expression,
                                                                         expected_salesforce_query_expression)

    def test_8(self):
        filter_expression = 'AccountNumber IN (3, 5, 9)'
        self.assertRaises(errors.InvalidFilterExpressionError,
                          self._test_conversion_from_filter_expression_to_salesforce_query,
                          filter_expression,
                          '')

    def test_9(self):
        filter_expression = 'AccountNumber between 1 AND 10'
        expected_salesforce_query_expression = 'AccountNumber > 1 and AccountNumber < 10'
        self._test_conversion_from_filter_expression_to_salesforce_query(filter_expression,
                                                                         expected_salesforce_query_expression)

    def test_10(self):
        filter_expression = 'AccountNumber = 1 or (UpdatedDate between 2020-03-05 and 2020-03-07)'
        expected_salesforce_query_expression = 'AccountNumber = 1 or UpdatedDate > 2020-03-05 and ' +\
                                               'UpdatedDate < 2020-03-07'
        self._test_conversion_from_filter_expression_to_salesforce_query(filter_expression,
                                                                         expected_salesforce_query_expression)

    def test_11(self):
        filter_expression = 'AccountNumber BETWEEN 5'
        self.assertRaises(errors.InvalidFilterExpressionError,
                          self._test_conversion_from_filter_expression_to_salesforce_query,
                          filter_expression,
                          '')

    def test_12(self):
        filter_expression = 'NotAField = 10'
        self.assertRaises(ValueError,
                          self._test_conversion_from_filter_expression_to_salesforce_query,
                          filter_expression,
                          '')
