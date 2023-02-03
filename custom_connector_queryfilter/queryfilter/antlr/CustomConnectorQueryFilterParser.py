# Generated from grammar/CustomConnectorQueryFilterParser.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\37")
        buf.write("\u00a6\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3e\n\3\f\3\16\3h")
        buf.write("\13\3\3\3\3\3\5\3l\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\7\3z\n\3\f\3\16\3}\13\3\3\4\3\4\3\5\3")
        buf.write("\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3")
        buf.write("\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\5\23\u00a2\n\23\3")
        buf.write("\24\3\24\3\24\2\3\4\25\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&\2\4\3\2\6\7\4\2\22\22\31\34\2\u00a8\2(\3\2")
        buf.write("\2\2\4k\3\2\2\2\6~\3\2\2\2\b\u0080\3\2\2\2\n\u0082\3\2")
        buf.write("\2\2\f\u0084\3\2\2\2\16\u0086\3\2\2\2\20\u0088\3\2\2\2")
        buf.write("\22\u008a\3\2\2\2\24\u008c\3\2\2\2\26\u008e\3\2\2\2\30")
        buf.write("\u0090\3\2\2\2\32\u0092\3\2\2\2\34\u0094\3\2\2\2\36\u0096")
        buf.write("\3\2\2\2 \u0098\3\2\2\2\"\u009a\3\2\2\2$\u00a1\3\2\2\2")
        buf.write("&\u00a3\3\2\2\2()\5\4\3\2)*\7\2\2\3*\3\3\2\2\2+,\b\3\1")
        buf.write("\2,-\7\20\2\2-.\5\4\3\2./\7\21\2\2/l\3\2\2\2\60\61\7\5")
        buf.write("\2\2\61l\5\4\3\22\62\63\5\34\17\2\63\64\5\6\4\2\64\65")
        buf.write("\5$\23\2\65l\3\2\2\2\66\67\5\34\17\2\678\5\b\5\289\5$")
        buf.write("\23\29l\3\2\2\2:;\5\34\17\2;<\5\n\6\2<=\5$\23\2=l\3\2")
        buf.write("\2\2>?\5\34\17\2?@\5\f\7\2@A\5$\23\2Al\3\2\2\2BC\5\34")
        buf.write("\17\2CD\5\16\b\2DE\5$\23\2El\3\2\2\2FG\5\34\17\2GH\5\16")
        buf.write("\b\2HI\5\32\16\2Il\3\2\2\2JK\5\34\17\2KL\5\20\t\2LM\5")
        buf.write("$\23\2Ml\3\2\2\2NO\5\34\17\2OP\5\20\t\2PQ\5\32\16\2Ql")
        buf.write("\3\2\2\2RS\5\34\17\2ST\5\22\n\2TU\5$\23\2Ul\3\2\2\2VW")
        buf.write("\5\34\17\2WX\5\24\13\2XY\5$\23\2YZ\5\26\f\2Z[\5$\23\2")
        buf.write("[l\3\2\2\2\\l\5\34\17\2]l\5$\23\2^_\5\34\17\2_`\5\36\20")
        buf.write("\2`a\7\20\2\2af\5$\23\2bc\7\25\2\2ce\5$\23\2db\3\2\2\2")
        buf.write("eh\3\2\2\2fd\3\2\2\2fg\3\2\2\2gi\3\2\2\2hf\3\2\2\2ij\7")
        buf.write("\21\2\2jl\3\2\2\2k+\3\2\2\2k\60\3\2\2\2k\62\3\2\2\2k\66")
        buf.write("\3\2\2\2k:\3\2\2\2k>\3\2\2\2kB\3\2\2\2kF\3\2\2\2kJ\3\2")
        buf.write("\2\2kN\3\2\2\2kR\3\2\2\2kV\3\2\2\2k\\\3\2\2\2k]\3\2\2")
        buf.write("\2k^\3\2\2\2l{\3\2\2\2mn\f\21\2\2no\5\26\f\2op\5\4\3\22")
        buf.write("pz\3\2\2\2qr\f\20\2\2rs\5\30\r\2st\5\4\3\21tz\3\2\2\2")
        buf.write("uv\f\23\2\2vw\5 \21\2wx\5&\24\2xz\3\2\2\2ym\3\2\2\2yq")
        buf.write("\3\2\2\2yu\3\2\2\2z}\3\2\2\2{y\3\2\2\2{|\3\2\2\2|\5\3")
        buf.write("\2\2\2}{\3\2\2\2~\177\7\b\2\2\177\7\3\2\2\2\u0080\u0081")
        buf.write("\7\t\2\2\u0081\t\3\2\2\2\u0082\u0083\7\n\2\2\u0083\13")
        buf.write("\3\2\2\2\u0084\u0085\7\13\2\2\u0085\r\3\2\2\2\u0086\u0087")
        buf.write("\7\f\2\2\u0087\17\3\2\2\2\u0088\u0089\7\r\2\2\u0089\21")
        buf.write("\3\2\2\2\u008a\u008b\7\16\2\2\u008b\23\3\2\2\2\u008c\u008d")
        buf.write("\7\17\2\2\u008d\25\3\2\2\2\u008e\u008f\7\3\2\2\u008f\27")
        buf.write("\3\2\2\2\u0090\u0091\7\4\2\2\u0091\31\3\2\2\2\u0092\u0093")
        buf.write("\t\2\2\2\u0093\33\3\2\2\2\u0094\u0095\7\26\2\2\u0095\35")
        buf.write("\3\2\2\2\u0096\u0097\7\23\2\2\u0097\37\3\2\2\2\u0098\u0099")
        buf.write("\7\24\2\2\u0099!\3\2\2\2\u009a\u009b\t\3\2\2\u009b#\3")
        buf.write("\2\2\2\u009c\u00a2\5\"\22\2\u009d\u00a2\7\27\2\2\u009e")
        buf.write("\u00a2\7\30\2\2\u009f\u00a2\7\36\2\2\u00a0\u00a2\7\37")
        buf.write("\2\2\u00a1\u009c\3\2\2\2\u00a1\u009d\3\2\2\2\u00a1\u009e")
        buf.write("\3\2\2\2\u00a1\u009f\3\2\2\2\u00a1\u00a0\3\2\2\2\u00a2")
        buf.write("%\3\2\2\2\u00a3\u00a4\7\27\2\2\u00a4\'\3\2\2\2\7fky{\u00a1")
        return buf.getvalue()


class CustomConnectorQueryFilterParser ( Parser ):

    grammarFileName = "CustomConnectorQueryFilterParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'>'", "'>='", "'<'", "'<='", 
                     "'='", "'!='", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'null'", "<INVALID>", "<INVALID>", "','" ]

    symbolicNames = [ "<INVALID>", "AND", "OR", "NOT", "TRUE", "FALSE", 
                      "GT", "GE", "LT", "LE", "EQ", "NE", "LIKE", "BETWEEN", 
                      "LPAREN", "RPAREN", "NULL", "IN", "LIMIT", "COMMA", 
                      "IDENTIFIER", "POS_INTEGER", "DECIMAL", "SINGLE_STRING", 
                      "DOUBLE_STRING", "EMPTY_SINGLE_STRING", "EMPTY_DOUBLE_STRING", 
                      "WS", "DATE", "DATETIME" ]

    RULE_queryfilter = 0
    RULE_expression = 1
    RULE_gtComparator = 2
    RULE_geComparator = 3
    RULE_ltComparator = 4
    RULE_leComparator = 5
    RULE_eqComparator = 6
    RULE_neComparator = 7
    RULE_likeComparator = 8
    RULE_betweenComparator = 9
    RULE_andBinary = 10
    RULE_orBinary = 11
    RULE_boolean = 12
    RULE_identifier = 13
    RULE_inOperator = 14
    RULE_limit = 15
    RULE_string = 16
    RULE_value = 17
    RULE_count = 18

    ruleNames =  [ "queryfilter", "expression", "gtComparator", "geComparator", 
                   "ltComparator", "leComparator", "eqComparator", "neComparator", 
                   "likeComparator", "betweenComparator", "andBinary", "orBinary", 
                   "boolean", "identifier", "inOperator", "limit", "string", 
                   "value", "count" ]

    EOF = Token.EOF
    AND=1
    OR=2
    NOT=3
    TRUE=4
    FALSE=5
    GT=6
    GE=7
    LT=8
    LE=9
    EQ=10
    NE=11
    LIKE=12
    BETWEEN=13
    LPAREN=14
    RPAREN=15
    NULL=16
    IN=17
    LIMIT=18
    COMMA=19
    IDENTIFIER=20
    POS_INTEGER=21
    DECIMAL=22
    SINGLE_STRING=23
    DOUBLE_STRING=24
    EMPTY_SINGLE_STRING=25
    EMPTY_DOUBLE_STRING=26
    WS=27
    DATE=28
    DATETIME=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class QueryfilterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.ExpressionContext,0)


        def EOF(self):
            return self.getToken(CustomConnectorQueryFilterParser.EOF, 0)

        def getRuleIndex(self):
            return CustomConnectorQueryFilterParser.RULE_queryfilter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQueryfilter" ):
                listener.enterQueryfilter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQueryfilter" ):
                listener.exitQueryfilter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQueryfilter" ):
                return visitor.visitQueryfilter(self)
            else:
                return visitor.visitChildren(self)




    def queryfilter(self):

        localctx = CustomConnectorQueryFilterParser.QueryfilterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_queryfilter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.expression(0)
            self.state = 39
            self.match(CustomConnectorQueryFilterParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CustomConnectorQueryFilterParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class LesserThanComparatorExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CustomConnectorQueryFilterParser.ExpressionContext
            super().__init__(parser)
            self.left = None # IdentifierContext
            self.op = None # LtComparatorContext
            self.right = None # ValueContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.IdentifierContext,0)

        def ltComparator(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.LtComparatorContext,0)

        def value(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLesserThanComparatorExpression" ):
                listener.enterLesserThanComparatorExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLesserThanComparatorExpression" ):
                listener.exitLesserThanComparatorExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLesserThanComparatorExpression" ):
                return visitor.visitLesserThanComparatorExpression(self)
            else:
                return visitor.visitChildren(self)


    class GreaterThanComparatorExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CustomConnectorQueryFilterParser.ExpressionContext
            super().__init__(parser)
            self.left = None # IdentifierContext
            self.op = None # GtComparatorContext
            self.right = None # ValueContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.IdentifierContext,0)

        def gtComparator(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.GtComparatorContext,0)

        def value(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreaterThanComparatorExpression" ):
                listener.enterGreaterThanComparatorExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreaterThanComparatorExpression" ):
                listener.exitGreaterThanComparatorExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreaterThanComparatorExpression" ):
                return visitor.visitGreaterThanComparatorExpression(self)
            else:
                return visitor.visitChildren(self)


    class BooleanEqualToComparatorExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CustomConnectorQueryFilterParser.ExpressionContext
            super().__init__(parser)
            self.left = None # IdentifierContext
            self.op = None # EqComparatorContext
            self.right = None # BooleanContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.IdentifierContext,0)

        def eqComparator(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.EqComparatorContext,0)

        def boolean(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.BooleanContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanEqualToComparatorExpression" ):
                listener.enterBooleanEqualToComparatorExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanEqualToComparatorExpression" ):
                listener.exitBooleanEqualToComparatorExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanEqualToComparatorExpression" ):
                return visitor.visitBooleanEqualToComparatorExpression(self)
            else:
                return visitor.visitChildren(self)


    class ValueExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CustomConnectorQueryFilterParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def value(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValueExpression" ):
                listener.enterValueExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValueExpression" ):
                listener.exitValueExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValueExpression" ):
                return visitor.visitValueExpression(self)
            else:
                return visitor.visitChildren(self)


    class BooleanNotEqualToComparatorExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CustomConnectorQueryFilterParser.ExpressionContext
            super().__init__(parser)
            self.left = None # IdentifierContext
            self.op = None # NeComparatorContext
            self.right = None # BooleanContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.IdentifierContext,0)

        def neComparator(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.NeComparatorContext,0)

        def boolean(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.BooleanContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanNotEqualToComparatorExpression" ):
                listener.enterBooleanNotEqualToComparatorExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanNotEqualToComparatorExpression" ):
                listener.exitBooleanNotEqualToComparatorExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanNotEqualToComparatorExpression" ):
                return visitor.visitBooleanNotEqualToComparatorExpression(self)
            else:
                return visitor.visitChildren(self)


    class IdentifierExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CustomConnectorQueryFilterParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.IdentifierContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifierExpression" ):
                listener.enterIdentifierExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifierExpression" ):
                listener.exitIdentifierExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierExpression" ):
                return visitor.visitIdentifierExpression(self)
            else:
                return visitor.visitChildren(self)


    class NotExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CustomConnectorQueryFilterParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(CustomConnectorQueryFilterParser.NOT, 0)
        def expression(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpression" ):
                listener.enterNotExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpression" ):
                listener.exitNotExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpression" ):
                return visitor.visitNotExpression(self)
            else:
                return visitor.visitChildren(self)


    class ParenExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CustomConnectorQueryFilterParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(CustomConnectorQueryFilterParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(CustomConnectorQueryFilterParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpression" ):
                listener.enterParenExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpression" ):
                listener.exitParenExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpression" ):
                return visitor.visitParenExpression(self)
            else:
                return visitor.visitChildren(self)


    class ORBinaryExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CustomConnectorQueryFilterParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.op = None # OrBinaryContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CustomConnectorQueryFilterParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CustomConnectorQueryFilterParser.ExpressionContext,i)

        def orBinary(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.OrBinaryContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterORBinaryExpression" ):
                listener.enterORBinaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitORBinaryExpression" ):
                listener.exitORBinaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitORBinaryExpression" ):
                return visitor.visitORBinaryExpression(self)
            else:
                return visitor.visitChildren(self)


    class LimitExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CustomConnectorQueryFilterParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.op = None # LimitContext
            self.right = None # CountContext
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.ExpressionContext,0)

        def limit(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.LimitContext,0)

        def count(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.CountContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLimitExpression" ):
                listener.enterLimitExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLimitExpression" ):
                listener.exitLimitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLimitExpression" ):
                return visitor.visitLimitExpression(self)
            else:
                return visitor.visitChildren(self)


    class EqualToComparatorExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CustomConnectorQueryFilterParser.ExpressionContext
            super().__init__(parser)
            self.left = None # IdentifierContext
            self.op = None # EqComparatorContext
            self.right = None # ValueContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.IdentifierContext,0)

        def eqComparator(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.EqComparatorContext,0)

        def value(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualToComparatorExpression" ):
                listener.enterEqualToComparatorExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualToComparatorExpression" ):
                listener.exitEqualToComparatorExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualToComparatorExpression" ):
                return visitor.visitEqualToComparatorExpression(self)
            else:
                return visitor.visitChildren(self)


    class BetweenExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CustomConnectorQueryFilterParser.ExpressionContext
            super().__init__(parser)
            self.left = None # IdentifierContext
            self.op = None # BetweenComparatorContext
            self.l1 = None # ValueContext
            self.op1 = None # AndBinaryContext
            self.right = None # ValueContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.IdentifierContext,0)

        def betweenComparator(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.BetweenComparatorContext,0)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CustomConnectorQueryFilterParser.ValueContext)
            else:
                return self.getTypedRuleContext(CustomConnectorQueryFilterParser.ValueContext,i)

        def andBinary(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.AndBinaryContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBetweenExpression" ):
                listener.enterBetweenExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBetweenExpression" ):
                listener.exitBetweenExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBetweenExpression" ):
                return visitor.visitBetweenExpression(self)
            else:
                return visitor.visitChildren(self)


    class InExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CustomConnectorQueryFilterParser.ExpressionContext
            super().__init__(parser)
            self.op = None # InOperatorContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.IdentifierContext,0)

        def LPAREN(self):
            return self.getToken(CustomConnectorQueryFilterParser.LPAREN, 0)
        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CustomConnectorQueryFilterParser.ValueContext)
            else:
                return self.getTypedRuleContext(CustomConnectorQueryFilterParser.ValueContext,i)

        def RPAREN(self):
            return self.getToken(CustomConnectorQueryFilterParser.RPAREN, 0)
        def inOperator(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.InOperatorContext,0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CustomConnectorQueryFilterParser.COMMA)
            else:
                return self.getToken(CustomConnectorQueryFilterParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInExpression" ):
                listener.enterInExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInExpression" ):
                listener.exitInExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInExpression" ):
                return visitor.visitInExpression(self)
            else:
                return visitor.visitChildren(self)


    class GreaterThanEqualToComparatorExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CustomConnectorQueryFilterParser.ExpressionContext
            super().__init__(parser)
            self.left = None # IdentifierContext
            self.op = None # GeComparatorContext
            self.right = None # ValueContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.IdentifierContext,0)

        def geComparator(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.GeComparatorContext,0)

        def value(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreaterThanEqualToComparatorExpression" ):
                listener.enterGreaterThanEqualToComparatorExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreaterThanEqualToComparatorExpression" ):
                listener.exitGreaterThanEqualToComparatorExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreaterThanEqualToComparatorExpression" ):
                return visitor.visitGreaterThanEqualToComparatorExpression(self)
            else:
                return visitor.visitChildren(self)


    class LikeComparatorExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CustomConnectorQueryFilterParser.ExpressionContext
            super().__init__(parser)
            self.left = None # IdentifierContext
            self.op = None # LikeComparatorContext
            self.right = None # ValueContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.IdentifierContext,0)

        def likeComparator(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.LikeComparatorContext,0)

        def value(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLikeComparatorExpression" ):
                listener.enterLikeComparatorExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLikeComparatorExpression" ):
                listener.exitLikeComparatorExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLikeComparatorExpression" ):
                return visitor.visitLikeComparatorExpression(self)
            else:
                return visitor.visitChildren(self)


    class LesserThanEqualToComparatorExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CustomConnectorQueryFilterParser.ExpressionContext
            super().__init__(parser)
            self.left = None # IdentifierContext
            self.op = None # LeComparatorContext
            self.right = None # ValueContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.IdentifierContext,0)

        def leComparator(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.LeComparatorContext,0)

        def value(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLesserThanEqualToComparatorExpression" ):
                listener.enterLesserThanEqualToComparatorExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLesserThanEqualToComparatorExpression" ):
                listener.exitLesserThanEqualToComparatorExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLesserThanEqualToComparatorExpression" ):
                return visitor.visitLesserThanEqualToComparatorExpression(self)
            else:
                return visitor.visitChildren(self)


    class NotEqualToComparatorExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CustomConnectorQueryFilterParser.ExpressionContext
            super().__init__(parser)
            self.left = None # IdentifierContext
            self.op = None # NeComparatorContext
            self.right = None # ValueContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.IdentifierContext,0)

        def neComparator(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.NeComparatorContext,0)

        def value(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotEqualToComparatorExpression" ):
                listener.enterNotEqualToComparatorExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotEqualToComparatorExpression" ):
                listener.exitNotEqualToComparatorExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotEqualToComparatorExpression" ):
                return visitor.visitNotEqualToComparatorExpression(self)
            else:
                return visitor.visitChildren(self)


    class ANDBinaryExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CustomConnectorQueryFilterParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.op = None # AndBinaryContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CustomConnectorQueryFilterParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CustomConnectorQueryFilterParser.ExpressionContext,i)

        def andBinary(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.AndBinaryContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterANDBinaryExpression" ):
                listener.enterANDBinaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitANDBinaryExpression" ):
                listener.exitANDBinaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitANDBinaryExpression" ):
                return visitor.visitANDBinaryExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CustomConnectorQueryFilterParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = CustomConnectorQueryFilterParser.ParenExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 42
                self.match(CustomConnectorQueryFilterParser.LPAREN)
                self.state = 43
                self.expression(0)
                self.state = 44
                self.match(CustomConnectorQueryFilterParser.RPAREN)
                pass

            elif la_ == 2:
                localctx = CustomConnectorQueryFilterParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 46
                self.match(CustomConnectorQueryFilterParser.NOT)
                self.state = 47
                self.expression(16)
                pass

            elif la_ == 3:
                localctx = CustomConnectorQueryFilterParser.GreaterThanComparatorExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 48
                localctx.left = self.identifier()
                self.state = 49
                localctx.op = self.gtComparator()
                self.state = 50
                localctx.right = self.value()
                pass

            elif la_ == 4:
                localctx = CustomConnectorQueryFilterParser.GreaterThanEqualToComparatorExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 52
                localctx.left = self.identifier()
                self.state = 53
                localctx.op = self.geComparator()
                self.state = 54
                localctx.right = self.value()
                pass

            elif la_ == 5:
                localctx = CustomConnectorQueryFilterParser.LesserThanComparatorExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 56
                localctx.left = self.identifier()
                self.state = 57
                localctx.op = self.ltComparator()
                self.state = 58
                localctx.right = self.value()
                pass

            elif la_ == 6:
                localctx = CustomConnectorQueryFilterParser.LesserThanEqualToComparatorExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 60
                localctx.left = self.identifier()
                self.state = 61
                localctx.op = self.leComparator()
                self.state = 62
                localctx.right = self.value()
                pass

            elif la_ == 7:
                localctx = CustomConnectorQueryFilterParser.EqualToComparatorExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 64
                localctx.left = self.identifier()
                self.state = 65
                localctx.op = self.eqComparator()
                self.state = 66
                localctx.right = self.value()
                pass

            elif la_ == 8:
                localctx = CustomConnectorQueryFilterParser.BooleanEqualToComparatorExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 68
                localctx.left = self.identifier()
                self.state = 69
                localctx.op = self.eqComparator()
                self.state = 70
                localctx.right = self.boolean()
                pass

            elif la_ == 9:
                localctx = CustomConnectorQueryFilterParser.NotEqualToComparatorExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 72
                localctx.left = self.identifier()
                self.state = 73
                localctx.op = self.neComparator()
                self.state = 74
                localctx.right = self.value()
                pass

            elif la_ == 10:
                localctx = CustomConnectorQueryFilterParser.BooleanNotEqualToComparatorExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 76
                localctx.left = self.identifier()
                self.state = 77
                localctx.op = self.neComparator()
                self.state = 78
                localctx.right = self.boolean()
                pass

            elif la_ == 11:
                localctx = CustomConnectorQueryFilterParser.LikeComparatorExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 80
                localctx.left = self.identifier()
                self.state = 81
                localctx.op = self.likeComparator()
                self.state = 82
                localctx.right = self.value()
                pass

            elif la_ == 12:
                localctx = CustomConnectorQueryFilterParser.BetweenExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 84
                localctx.left = self.identifier()
                self.state = 85
                localctx.op = self.betweenComparator()

                self.state = 86
                localctx.l1 = self.value()
                self.state = 87
                localctx.op1 = self.andBinary()
                self.state = 88
                localctx.right = self.value()
                pass

            elif la_ == 13:
                localctx = CustomConnectorQueryFilterParser.IdentifierExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 90
                self.identifier()
                pass

            elif la_ == 14:
                localctx = CustomConnectorQueryFilterParser.ValueExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 91
                self.value()
                pass

            elif la_ == 15:
                localctx = CustomConnectorQueryFilterParser.InExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 92
                self.identifier()
                self.state = 93
                localctx.op = self.inOperator()
                self.state = 94
                self.match(CustomConnectorQueryFilterParser.LPAREN)
                self.state = 95
                self.value()
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CustomConnectorQueryFilterParser.COMMA:
                    self.state = 96
                    self.match(CustomConnectorQueryFilterParser.COMMA)
                    self.state = 97
                    self.value()
                    self.state = 102
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 103
                self.match(CustomConnectorQueryFilterParser.RPAREN)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 121
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 119
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = CustomConnectorQueryFilterParser.ANDBinaryExpressionContext(self, CustomConnectorQueryFilterParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 107
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 108
                        localctx.op = self.andBinary()
                        self.state = 109
                        localctx.right = self.expression(16)
                        pass

                    elif la_ == 2:
                        localctx = CustomConnectorQueryFilterParser.ORBinaryExpressionContext(self, CustomConnectorQueryFilterParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 111
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 112
                        localctx.op = self.orBinary()
                        self.state = 113
                        localctx.right = self.expression(15)
                        pass

                    elif la_ == 3:
                        localctx = CustomConnectorQueryFilterParser.LimitExpressionContext(self, CustomConnectorQueryFilterParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 115
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 116
                        localctx.op = self.limit()
                        self.state = 117
                        localctx.right = self.count()
                        pass

             
                self.state = 123
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class GtComparatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GT(self):
            return self.getToken(CustomConnectorQueryFilterParser.GT, 0)

        def getRuleIndex(self):
            return CustomConnectorQueryFilterParser.RULE_gtComparator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGtComparator" ):
                listener.enterGtComparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGtComparator" ):
                listener.exitGtComparator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGtComparator" ):
                return visitor.visitGtComparator(self)
            else:
                return visitor.visitChildren(self)




    def gtComparator(self):

        localctx = CustomConnectorQueryFilterParser.GtComparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_gtComparator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(CustomConnectorQueryFilterParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GeComparatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GE(self):
            return self.getToken(CustomConnectorQueryFilterParser.GE, 0)

        def getRuleIndex(self):
            return CustomConnectorQueryFilterParser.RULE_geComparator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGeComparator" ):
                listener.enterGeComparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGeComparator" ):
                listener.exitGeComparator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGeComparator" ):
                return visitor.visitGeComparator(self)
            else:
                return visitor.visitChildren(self)




    def geComparator(self):

        localctx = CustomConnectorQueryFilterParser.GeComparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_geComparator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(CustomConnectorQueryFilterParser.GE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LtComparatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(CustomConnectorQueryFilterParser.LT, 0)

        def getRuleIndex(self):
            return CustomConnectorQueryFilterParser.RULE_ltComparator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLtComparator" ):
                listener.enterLtComparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLtComparator" ):
                listener.exitLtComparator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLtComparator" ):
                return visitor.visitLtComparator(self)
            else:
                return visitor.visitChildren(self)




    def ltComparator(self):

        localctx = CustomConnectorQueryFilterParser.LtComparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ltComparator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(CustomConnectorQueryFilterParser.LT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LeComparatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LE(self):
            return self.getToken(CustomConnectorQueryFilterParser.LE, 0)

        def getRuleIndex(self):
            return CustomConnectorQueryFilterParser.RULE_leComparator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLeComparator" ):
                listener.enterLeComparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLeComparator" ):
                listener.exitLeComparator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeComparator" ):
                return visitor.visitLeComparator(self)
            else:
                return visitor.visitChildren(self)




    def leComparator(self):

        localctx = CustomConnectorQueryFilterParser.LeComparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_leComparator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(CustomConnectorQueryFilterParser.LE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqComparatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(CustomConnectorQueryFilterParser.EQ, 0)

        def getRuleIndex(self):
            return CustomConnectorQueryFilterParser.RULE_eqComparator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqComparator" ):
                listener.enterEqComparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqComparator" ):
                listener.exitEqComparator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqComparator" ):
                return visitor.visitEqComparator(self)
            else:
                return visitor.visitChildren(self)




    def eqComparator(self):

        localctx = CustomConnectorQueryFilterParser.EqComparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_eqComparator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(CustomConnectorQueryFilterParser.EQ)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NeComparatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NE(self):
            return self.getToken(CustomConnectorQueryFilterParser.NE, 0)

        def getRuleIndex(self):
            return CustomConnectorQueryFilterParser.RULE_neComparator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNeComparator" ):
                listener.enterNeComparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNeComparator" ):
                listener.exitNeComparator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNeComparator" ):
                return visitor.visitNeComparator(self)
            else:
                return visitor.visitChildren(self)




    def neComparator(self):

        localctx = CustomConnectorQueryFilterParser.NeComparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_neComparator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(CustomConnectorQueryFilterParser.NE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LikeComparatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIKE(self):
            return self.getToken(CustomConnectorQueryFilterParser.LIKE, 0)

        def getRuleIndex(self):
            return CustomConnectorQueryFilterParser.RULE_likeComparator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLikeComparator" ):
                listener.enterLikeComparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLikeComparator" ):
                listener.exitLikeComparator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLikeComparator" ):
                return visitor.visitLikeComparator(self)
            else:
                return visitor.visitChildren(self)




    def likeComparator(self):

        localctx = CustomConnectorQueryFilterParser.LikeComparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_likeComparator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(CustomConnectorQueryFilterParser.LIKE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BetweenComparatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BETWEEN(self):
            return self.getToken(CustomConnectorQueryFilterParser.BETWEEN, 0)

        def getRuleIndex(self):
            return CustomConnectorQueryFilterParser.RULE_betweenComparator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBetweenComparator" ):
                listener.enterBetweenComparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBetweenComparator" ):
                listener.exitBetweenComparator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBetweenComparator" ):
                return visitor.visitBetweenComparator(self)
            else:
                return visitor.visitChildren(self)




    def betweenComparator(self):

        localctx = CustomConnectorQueryFilterParser.BetweenComparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_betweenComparator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(CustomConnectorQueryFilterParser.BETWEEN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndBinaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(CustomConnectorQueryFilterParser.AND, 0)

        def getRuleIndex(self):
            return CustomConnectorQueryFilterParser.RULE_andBinary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndBinary" ):
                listener.enterAndBinary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndBinary" ):
                listener.exitAndBinary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndBinary" ):
                return visitor.visitAndBinary(self)
            else:
                return visitor.visitChildren(self)




    def andBinary(self):

        localctx = CustomConnectorQueryFilterParser.AndBinaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_andBinary)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(CustomConnectorQueryFilterParser.AND)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrBinaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OR(self):
            return self.getToken(CustomConnectorQueryFilterParser.OR, 0)

        def getRuleIndex(self):
            return CustomConnectorQueryFilterParser.RULE_orBinary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrBinary" ):
                listener.enterOrBinary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrBinary" ):
                listener.exitOrBinary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrBinary" ):
                return visitor.visitOrBinary(self)
            else:
                return visitor.visitChildren(self)




    def orBinary(self):

        localctx = CustomConnectorQueryFilterParser.OrBinaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_orBinary)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(CustomConnectorQueryFilterParser.OR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(CustomConnectorQueryFilterParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(CustomConnectorQueryFilterParser.FALSE, 0)

        def getRuleIndex(self):
            return CustomConnectorQueryFilterParser.RULE_boolean

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean" ):
                listener.enterBoolean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean" ):
                listener.exitBoolean(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean" ):
                return visitor.visitBoolean(self)
            else:
                return visitor.visitChildren(self)




    def boolean(self):

        localctx = CustomConnectorQueryFilterParser.BooleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_boolean)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            _la = self._input.LA(1)
            if not(_la==CustomConnectorQueryFilterParser.TRUE or _la==CustomConnectorQueryFilterParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CustomConnectorQueryFilterParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return CustomConnectorQueryFilterParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = CustomConnectorQueryFilterParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(CustomConnectorQueryFilterParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IN(self):
            return self.getToken(CustomConnectorQueryFilterParser.IN, 0)

        def getRuleIndex(self):
            return CustomConnectorQueryFilterParser.RULE_inOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInOperator" ):
                listener.enterInOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInOperator" ):
                listener.exitInOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInOperator" ):
                return visitor.visitInOperator(self)
            else:
                return visitor.visitChildren(self)




    def inOperator(self):

        localctx = CustomConnectorQueryFilterParser.InOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_inOperator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(CustomConnectorQueryFilterParser.IN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LimitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIMIT(self):
            return self.getToken(CustomConnectorQueryFilterParser.LIMIT, 0)

        def getRuleIndex(self):
            return CustomConnectorQueryFilterParser.RULE_limit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLimit" ):
                listener.enterLimit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLimit" ):
                listener.exitLimit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLimit" ):
                return visitor.visitLimit(self)
            else:
                return visitor.visitChildren(self)




    def limit(self):

        localctx = CustomConnectorQueryFilterParser.LimitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_limit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(CustomConnectorQueryFilterParser.LIMIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINGLE_STRING(self):
            return self.getToken(CustomConnectorQueryFilterParser.SINGLE_STRING, 0)

        def DOUBLE_STRING(self):
            return self.getToken(CustomConnectorQueryFilterParser.DOUBLE_STRING, 0)

        def EMPTY_DOUBLE_STRING(self):
            return self.getToken(CustomConnectorQueryFilterParser.EMPTY_DOUBLE_STRING, 0)

        def EMPTY_SINGLE_STRING(self):
            return self.getToken(CustomConnectorQueryFilterParser.EMPTY_SINGLE_STRING, 0)

        def NULL(self):
            return self.getToken(CustomConnectorQueryFilterParser.NULL, 0)

        def getRuleIndex(self):
            return CustomConnectorQueryFilterParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)




    def string(self):

        localctx = CustomConnectorQueryFilterParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CustomConnectorQueryFilterParser.NULL) | (1 << CustomConnectorQueryFilterParser.SINGLE_STRING) | (1 << CustomConnectorQueryFilterParser.DOUBLE_STRING) | (1 << CustomConnectorQueryFilterParser.EMPTY_SINGLE_STRING) | (1 << CustomConnectorQueryFilterParser.EMPTY_DOUBLE_STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CustomConnectorQueryFilterParser.RULE_value

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StringValueExpressionContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CustomConnectorQueryFilterParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def string(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.StringContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringValueExpression" ):
                listener.enterStringValueExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringValueExpression" ):
                listener.exitStringValueExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringValueExpression" ):
                return visitor.visitStringValueExpression(self)
            else:
                return visitor.visitChildren(self)


    class DecimalValueExpressionContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CustomConnectorQueryFilterParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def POS_INTEGER(self):
            return self.getToken(CustomConnectorQueryFilterParser.POS_INTEGER, 0)
        def DECIMAL(self):
            return self.getToken(CustomConnectorQueryFilterParser.DECIMAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecimalValueExpression" ):
                listener.enterDecimalValueExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecimalValueExpression" ):
                listener.exitDecimalValueExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecimalValueExpression" ):
                return visitor.visitDecimalValueExpression(self)
            else:
                return visitor.visitChildren(self)


    class IsoDateContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CustomConnectorQueryFilterParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DATE(self):
            return self.getToken(CustomConnectorQueryFilterParser.DATE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIsoDate" ):
                listener.enterIsoDate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIsoDate" ):
                listener.exitIsoDate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIsoDate" ):
                return visitor.visitIsoDate(self)
            else:
                return visitor.visitChildren(self)


    class IsoDateTimeContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CustomConnectorQueryFilterParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DATETIME(self):
            return self.getToken(CustomConnectorQueryFilterParser.DATETIME, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIsoDateTime" ):
                listener.enterIsoDateTime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIsoDateTime" ):
                listener.exitIsoDateTime(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIsoDateTime" ):
                return visitor.visitIsoDateTime(self)
            else:
                return visitor.visitChildren(self)



    def value(self):

        localctx = CustomConnectorQueryFilterParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_value)
        try:
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CustomConnectorQueryFilterParser.NULL, CustomConnectorQueryFilterParser.SINGLE_STRING, CustomConnectorQueryFilterParser.DOUBLE_STRING, CustomConnectorQueryFilterParser.EMPTY_SINGLE_STRING, CustomConnectorQueryFilterParser.EMPTY_DOUBLE_STRING]:
                localctx = CustomConnectorQueryFilterParser.StringValueExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.string()
                pass
            elif token in [CustomConnectorQueryFilterParser.POS_INTEGER]:
                localctx = CustomConnectorQueryFilterParser.DecimalValueExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.match(CustomConnectorQueryFilterParser.POS_INTEGER)
                pass
            elif token in [CustomConnectorQueryFilterParser.DECIMAL]:
                localctx = CustomConnectorQueryFilterParser.DecimalValueExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 156
                self.match(CustomConnectorQueryFilterParser.DECIMAL)
                pass
            elif token in [CustomConnectorQueryFilterParser.DATE]:
                localctx = CustomConnectorQueryFilterParser.IsoDateContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 157
                self.match(CustomConnectorQueryFilterParser.DATE)
                pass
            elif token in [CustomConnectorQueryFilterParser.DATETIME]:
                localctx = CustomConnectorQueryFilterParser.IsoDateTimeContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 158
                self.match(CustomConnectorQueryFilterParser.DATETIME)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CountContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CustomConnectorQueryFilterParser.RULE_count

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CountValueExpressionContext(CountContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CustomConnectorQueryFilterParser.CountContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def POS_INTEGER(self):
            return self.getToken(CustomConnectorQueryFilterParser.POS_INTEGER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCountValueExpression" ):
                listener.enterCountValueExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCountValueExpression" ):
                listener.exitCountValueExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCountValueExpression" ):
                return visitor.visitCountValueExpression(self)
            else:
                return visitor.visitChildren(self)



    def count(self):

        localctx = CustomConnectorQueryFilterParser.CountContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_count)
        try:
            localctx = CustomConnectorQueryFilterParser.CountValueExpressionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(CustomConnectorQueryFilterParser.POS_INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 17)
         




