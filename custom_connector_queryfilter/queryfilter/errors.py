from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import RecognitionException
from antlr4.Recognizer import Recognizer
from antlr4.Parser import Parser

from io import StringIO

class InvalidFilterExpressionError(Exception):
    """This error is raised when an invalid filter expression is given as input to the query expression parser."""
    pass

class SyntaxErrorReporter(ErrorListener):
    """This class is responsible for collecting and reporting syntax errors in passed filter expression in the input
    request.
    Note: This class is not thread safe.

    """
    def __init__(self):
        self.has_error = False
        self.syntax_errors = StringIO()

    def syntaxError(self,
                    parser: Parser,
                    offending_symbol: object,
                    line: int,
                    char_position_in_line: int,
                    msg: str,
                    e: RecognitionException):
        self.has_error = True
        stack = reversed(parser.getRuleInvocationStack())
        error = f'rule stack: {stack} line {line}:{char_position_in_line} at {offending_symbol}:{msg}'
        self.syntax_errors.write(error)
