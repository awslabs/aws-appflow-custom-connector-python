import unittest
import custom_connector_queryfilter.queryfilter.parse_tree_builder as parse_tree_builder
from custom_connector_queryfilter.queryfilter.errors import InvalidFilterExpressionError

class CustomConnectorParseTreeTest(unittest.TestCase):
    """Unit tests for parse_tree_builder."""
    def _test_parse_tree_with_valid_filter_expression(self, filter_expression):
        parse_tree_builder.parse(filter_expression)  # Should not raise an exception

    def _test_parse_tree_with_invalid_filter_expression(self, filter_expression):
        self.assertRaises(InvalidFilterExpressionError, parse_tree_builder.parse, filter_expression)

    def test_valid_expression_1(self):
        self._test_parse_tree_with_valid_filter_expression('os = "mojave"')

    def test_valid_expression_2(self):
        self._test_parse_tree_with_valid_filter_expression('os != "mojave"')

    def test_valid_expression_3(self):
        self._test_parse_tree_with_valid_filter_expression('accountId > 90')

    def test_valid_expression_4(self):
        self._test_parse_tree_with_valid_filter_expression('dateRange BETWEEN 1611639470000 AND 1611639476298')

    def test_valid_expression_5(self):
        self._test_parse_tree_with_valid_filter_expression('date BETWEEN 1511630000000 AND 1611639476298')

    def test_valid_expression_6(self):
        self._test_parse_tree_with_valid_filter_expression('time between 1511630000000 AND 1611639476298')

    def test_valid_expression_7(self):
        self._test_parse_tree_with_valid_filter_expression('accountId < 100')

    def test_valid_expression_8(self):
        self._test_parse_tree_with_valid_filter_expression('accountId >= 90')

    def test_valid_expression_9(self):
        self._test_parse_tree_with_valid_filter_expression('accountId <= 100')

    def test_valid_expression_10(self):
        self._test_parse_tree_with_valid_filter_expression('accountId BETWEEN 90 AND 100')

    def test_valid_expression_11(self):
        self._test_parse_tree_with_valid_filter_expression('os CONTAINS "mojave"')

    def test_valid_expression_12(self):
        self._test_parse_tree_with_valid_filter_expression('os CONTAINS "moj%ave"')

    def test_valid_expression_13(self):
        self._test_parse_tree_with_valid_filter_expression('os = "mojave" and app = "mo"')

    def test_valid_expression_14(self):
        self._test_parse_tree_with_valid_filter_expression('os = "mojave" OR app = "mo"')

    def test_valid_expression_15(self):
        self._test_parse_tree_with_valid_filter_expression('(os = "mojave" AND app = "mo")' +
                                                           ' and (os = "mojave" OR app = "mo")')

    def test_valid_expression_16(self):
        self._test_parse_tree_with_valid_filter_expression('(os = "mojave" AND app = "mo")' +
                                                           ' or (os = "mojave" OR app = "mo")')

    def test_valid_expression_17(self):
        self._test_parse_tree_with_valid_filter_expression('accountId in (100, 90, 70)')

    def test_valid_expression_18(self):
        self._test_parse_tree_with_valid_filter_expression('date between 2021-04-20 and 2021-04-21')

    def test_valid_expression_19(self):
        self._test_parse_tree_with_valid_filter_expression('date between 2021-04-20T12:30:45Z' +
                                                           ' and 2021-04-20T15:45:49.234Z')

    def test_valid_expression_20(self):
        self._test_parse_tree_with_valid_filter_expression('(accountId > 100 and ((date < 2021-04-20T12:30:45Z and ' +
                                                           'date > 2021-04-21T15:45:49.234Z) and accountId < 200))')

    def test_valid_expression_21(self):
        self._test_parse_tree_with_valid_filter_expression('overrides = true or accountFlag != false')

    def test_valid_expression_22(self):
        self._test_parse_tree_with_valid_filter_expression('overrides != true')

    def test_valid_expression_23(self):
        self._test_parse_tree_with_valid_filter_expression('date > 2020-10-05T12:05:34Z')

    def test_invalid_expression_1(self):
        self._test_parse_tree_with_invalid_filter_expression('os == "mojave"')

    def test_invalid_expression_2(self):
        self._test_parse_tree_with_invalid_filter_expression('os <> "mojave"')

    def test_invalid_expression_3(self):
        self._test_parse_tree_with_invalid_filter_expression('accountId => 90')

    def test_invalid_expression_4(self):
        self._test_parse_tree_with_invalid_filter_expression('dateRange in 1611639470000 AND 1611639476298')

    def test_invalid_expression_5(self):
        self._test_parse_tree_with_invalid_filter_expression('date FROM 1611639470000 TO 1611639476298')

    def test_invalid_expression_6(self):
        self._test_parse_tree_with_invalid_filter_expression('time Between 1611639470000 and 1611639476298')

    def test_invalid_expression_7(self):
        self._test_parse_tree_with_invalid_filter_expression('os CONTAIN "mojave"')

    def test_invalid_expression_8(self):
        self._test_parse_tree_with_invalid_filter_expression('os CONTAINS "moj%ave')

    def test_invalid_expression_9(self):
        self._test_parse_tree_with_invalid_filter_expression('accountId in (id, "90", 70)')

    def test_invalid_expression_10(self):
        self._test_parse_tree_with_invalid_filter_expression('accountId in (true)')

    def test_invalid_expression_11(self):
        self._test_parse_tree_with_invalid_filter_expression('date > 2021-04-203')

    def test_invalid_expression_12(self):
        self._test_parse_tree_with_invalid_filter_expression('date > 2021-04-20T20:30')

    def test_invalid_expression_13(self):
        self._test_parse_tree_with_invalid_filter_expression('date > 2021-04_20T20:30:20.9999+26')

    def test_invalid_expression_14(self):
        self._test_parse_tree_with_invalid_filter_expression('date > 2021-04_20T20:30:20.9999+12:23')

    def test_invalid_expression_15(self):
        self._test_parse_tree_with_invalid_filter_expression('date > 2021-04-20T20:30:20.9999-12:23')
