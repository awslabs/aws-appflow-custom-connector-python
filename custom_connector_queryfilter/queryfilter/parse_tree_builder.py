from antlr4.tree.Tree import ParseTree
from antlr4 import CommonTokenStream, InputStream
from custom_connector_queryfilter.queryfilter.antlr.CustomConnectorQueryFilterLexer import CustomConnectorQueryFilterLexer
from custom_connector_queryfilter.queryfilter.antlr.CustomConnectorQueryFilterParser import CustomConnectorQueryFilterParser
from custom_connector_queryfilter.queryfilter.errors import SyntaxErrorReporter, InvalidFilterExpressionError

def parse(filter_expression: str) -> ParseTree:
    """Helper function to validate and construct a parse tree for a given filter expression."""
    assert filter_expression is not None, "Filter expression cannot be empty"

    input_stream = InputStream(filter_expression)
    lexer = CustomConnectorQueryFilterLexer(input_stream)
    common_token_stream = CommonTokenStream(lexer)
    parser = CustomConnectorQueryFilterParser(common_token_stream)

    parser.removeErrorListeners()  # Remove any pre-existing error listeners and register custom listeners
    syntax_error_reporter = SyntaxErrorReporter()
    parser.addErrorListener(syntax_error_reporter)

    tree = parser.queryfilter()
    if syntax_error_reporter.has_error:
        raise InvalidFilterExpressionError('Filter expression has the following syntax errors :',
                                           syntax_error_reporter.syntax_errors.getvalue())
    return tree
