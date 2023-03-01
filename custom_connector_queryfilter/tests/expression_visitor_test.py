import unittest
from custom_connector_queryfilter.queryfilter.parse_tree_builder import parse
from custom_connector_queryfilter.queryfilter.antlr.CustomConnectorQueryFilterParserVisitor import CustomConnectorQueryFilterParserVisitor


class TestVisitor(CustomConnectorQueryFilterParserVisitor):
    def __init__(self):
        self.count_of_expressions_visited = 0

    def visit(self, tree):
        self.count_of_expressions_visited = 0
        super().visit(tree)
        return self.count_of_expressions_visited

    def visitLesserThanComparatorExpression(self, ctx):
        self.count_of_expressions_visited += 1
        return super().visitLesserThanComparatorExpression(ctx)

    def visitGreaterThanComparatorExpression(self, ctx):
        self.count_of_expressions_visited += 1
        return super().visitGreaterThanComparatorExpression(ctx)

    def visitValueExpression(self, ctx):
        self.count_of_expressions_visited += 1
        return super().visitValueExpression(ctx)

    def visitIdentifierExpression(self, ctx):
        return super().visitIdentifierExpression(ctx)

    def visitNotExpression(self, ctx):
        self.count_of_expressions_visited += 1
        return super().visitNotExpression(ctx)

    def visitParenExpression(self, ctx):
        return super().visitParenExpression(ctx)

    def visitORBinaryExpression(self, ctx):
        self.count_of_expressions_visited += 1
        return super().visitORBinaryExpression(ctx)

    def visitEqualToComparatorExpression(self, ctx):
        self.count_of_expressions_visited += 1
        return super().visitEqualToComparatorExpression(ctx)

    def visitBetweenExpression(self, ctx):
        self.count_of_expressions_visited += 1
        return super().visitBetweenExpression(ctx)

    def visitInExpression(self, ctx):
        self.count_of_expressions_visited += 1
        return super().visitInExpression(ctx)

    def visitGreaterThanEqualToComparatorExpression(self, ctx):
        self.count_of_expressions_visited += 1
        return super().visitGreaterThanEqualToComparatorExpression(ctx)

    def visitLikeComparatorExpression(self, ctx):
        self.count_of_expressions_visited += 1
        return super().visitLikeComparatorExpression(ctx)

    def visitLesserThanEqualToComparatorExpression(self, ctx):
        self.count_of_expressions_visited += 1
        return super().visitLesserThanEqualToComparatorExpression(ctx)

    def visitNotEqualToComparatorExpression(self, ctx):
        self.count_of_expressions_visited += 1
        return super().visitNotEqualToComparatorExpression(ctx)

    def visitANDBinaryExpression(self, ctx):
        self.count_of_expressions_visited += 1
        return super().visitANDBinaryExpression(ctx)

    def visitStringValueExpression(self, ctx):
        self.count_of_expressions_visited += 1
        return super().visitStringValueExpression(ctx)

    def visitDecimalValueExpression(self, ctx):
        self.count_of_expressions_visited += 1
        return super().visitDecimalValueExpression(ctx)

    def visitIsoDate(self, ctx):
        self.count_of_expressions_visited += 1
        return super().visitIsoDate(ctx)

    def visitIsoDateTime(self, ctx):
        self.count_of_expressions_visited += 1
        return super().visitIsoDateTime(ctx)

    def visitLimit(self, ctx):
        self.count_of_expressions_visited += 1
        return super().visitLimit(ctx)

    def visitCountValueExpression(self, ctx):
        self.count_of_expressions_visited += 1
        return super().visitCountValueExpression(ctx)


class QueryFilterExpressionVisitorTest(unittest.TestCase):
    def __init__(self, method_name='runTest'):
        self.test_visitor = TestVisitor()
        super().__init__(method_name)

    def _test_count_of_expression_visited(self, filter_expression: str, expected_count_of_expression_visited: int):
        parse_tree = parse(filter_expression)
        visited = self.test_visitor.visit(parse_tree)
        self.assertEqual(expected_count_of_expression_visited, visited)

    def test_expressions_visited(self):
        cases = [
            ('os = "mojave"', 2),
            ('os != "mojave"', 2),
            ('accountId > 90', 2),
            ('LIMIT 100', 2),
            ('dateRange BETWEEN 1611639470000 AND 1611639476298', 3),
            ('date BETWEEN 1511630000000 AND 1611639476298', 3),
            ('time between 1511630000000 AND 1611639476298', 3),
            ('accountId < 100', 2),
            ('accountId >= 90', 2),
            ('accountId >= 90 LIMIT 100', 4),
            ('accountId <= 100', 2),
            ('accountId BETWEEN 90 AND 100', 3),
            ('os CONTAINS "mojave"', 2),
            ('os CONTAINS "moj%ave"', 2),
            ('os = "mojave" and app = "mo"', 5),
            ('os = "mojave" OR app = "mo"', 5),
            ('(os = "mojave" AND app = "mo") and (os = "mojave" OR app = "mo")', 11),
            ('(os = "mojave" AND app = "mo") or (os = "mojave" OR app = "mo")', 11),
            ('accountId in (100, 90, 70)', 4),
            ('date between 2021-04-20 and 2021-04-21', 3),
            ('date between 2021-04-20T12:30:45Z and 2021-04-20T15:45:49.234Z', 3),
            ('(accountId > 100 and ((date < 2021-04-20T12:30:45Z and date > 2021-04-21T15:45:49.234Z) and ' +
             'accountId < 200))', 11)
        ]
        for expression, count in cases:
            with self.subTest(expression=expression, count=count):
                print((expression, count))
                self._test_count_of_expression_visited(expression, count)
