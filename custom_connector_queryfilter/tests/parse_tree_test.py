import unittest
import custom_connector_queryfilter.queryfilter.parse_tree_builder as parse_tree_builder
from custom_connector_queryfilter.queryfilter.errors import InvalidFilterExpressionError


class CustomConnectorParseTreeTest(unittest.TestCase):
    """Unit tests for parse_tree_builder."""
    def _test_parse_tree_with_valid_filter_expression(self, filter_expression):
        parse_tree_builder.parse(filter_expression)  # Should not raise an exception

    def _test_parse_tree_with_invalid_filter_expression(self, filter_expression):
        self.assertRaises(InvalidFilterExpressionError, parse_tree_builder.parse, filter_expression)

    def test_valid_expression(self):
        expressions = [
            'os = "mojave"',
            'os != "mojave"',
            "accountId > 90",
            "LIMIT 100",
            "dateRange BETWEEN 1611639470000 AND 1611639476298",
            "date BETWEEN 1511630000000 AND 1611639476298",
            "time between 1511630000000 AND 1611639476298",
            "accountId < 100",
            "accountId >= 90",
            "accountId <= 100",
            "accountId <= 100 LIMIT 100",
            "accountId BETWEEN 90 AND 100",
            "accountId BETWEEN 90 AND 100 LIMIT 100",
            'os CONTAINS "mojave"',
            'os CONTAINS "moj%ave"',
            'os = "mojave" and app = "mo"',
            'os = "mojave" OR app = "mo"',
            '(os = "mojave" AND app = "mo") and (os = "mojave" OR app = "mo")',
            '(os = "mojave" AND app = "mo") or (os = "mojave" OR app = "mo")',
            "accountId in (100, 90, 70)",
            "date between 2021-04-20 and 2021-04-21",
            'date between 2021-04-20T12:30:45Z and 2021-04-20T15:45:49.234Z',
            '(accountId > 100 and ((date < 2021-04-20T12:30:45Z and date > 2021-04-21T15:45:49.234Z) and ' +
            'accountId < 200))',
            "overrides = true or accountFlag != false",
            "overrides != true",
            "date > 2020-10-05T12:05:34Z"
        ]
        for expr in expressions:
            with self.subTest(expression=expr):
                print(expr)
                self._test_parse_tree_with_valid_filter_expression(expr)

    def test_invalid_expression(self):
        expressions = [
            'os == "mojave"',
            'os <> "mojave"',
            "LIMIT 100 LIMIT 100",
            "accountId => 90",
            "accountId => 90 LIMIT",
            "accountId => 90 LIMIT 0",
            "accountId => 90 LIMIT -1",
            "accountId => 90 LIMIT 1.5",
            "accountId => 90 LIMIT abc",
            "dateRange in 1611639470000 AND 1611639476298",
            "date FROM 1611639470000 TO 1611639476298",
            "time Between 1611639470000 and 1611639476298",
            'os CONTAIN "mojave"',
            'os CONTAINS "moj%ave',
            'accountId in (id, "90", 70)',
            "accountId in (true)",
            "date > 2021-04-203",
            "date > 2021-04-20T20:30",
            "date > 2021-04_20T20:30:20.9999+26",
            "date > 2021-04_20T20:30:20.9999+12:23",
            "date > 2021-04-20T20:30:20.9999-12:23"
        ]
        for expr in expressions:
            with self.subTest(expression=expr):
                print(expr)
                self._test_parse_tree_with_invalid_filter_expression(expr)
