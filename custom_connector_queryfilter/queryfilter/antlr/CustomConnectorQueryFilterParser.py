# Generated from CustomConnectorQueryFilterParser.g4 by ANTLR 4.9.3
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
        buf.write("\u00b2\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\3\2\3\2\3\2\3\2\3\2\3\2\5\2\61\n")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3:\n\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7")
        buf.write("\4u\n\4\f\4\16\4x\13\4\3\4\3\4\5\4|\n\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\7\4\u0086\n\4\f\4\16\4\u0089\13\4\3")
        buf.write("\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3")
        buf.write("\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21")
        buf.write("\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3\24\3\24\5\24")
        buf.write("\u00ae\n\24\3\25\3\25\3\25\2\3\6\26\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(\2\4\3\2\6\7\4\2\22\22\31\34")
        buf.write("\2\u00b4\2\60\3\2\2\2\49\3\2\2\2\6{\3\2\2\2\b\u008a\3")
        buf.write("\2\2\2\n\u008c\3\2\2\2\f\u008e\3\2\2\2\16\u0090\3\2\2")
        buf.write("\2\20\u0092\3\2\2\2\22\u0094\3\2\2\2\24\u0096\3\2\2\2")
        buf.write("\26\u0098\3\2\2\2\30\u009a\3\2\2\2\32\u009c\3\2\2\2\34")
        buf.write("\u009e\3\2\2\2\36\u00a0\3\2\2\2 \u00a2\3\2\2\2\"\u00a4")
        buf.write("\3\2\2\2$\u00a6\3\2\2\2&\u00ad\3\2\2\2(\u00af\3\2\2\2")
        buf.write("*+\5\6\4\2+,\7\2\2\3,\61\3\2\2\2-.\5\4\3\2./\7\2\2\3/")
        buf.write("\61\3\2\2\2\60*\3\2\2\2\60-\3\2\2\2\61\3\3\2\2\2\62\63")
        buf.write("\5\"\22\2\63\64\5(\25\2\64:\3\2\2\2\65\66\5\6\4\2\66\67")
        buf.write("\5\"\22\2\678\5(\25\28:\3\2\2\29\62\3\2\2\29\65\3\2\2")
        buf.write("\2:\5\3\2\2\2;<\b\4\1\2<=\7\20\2\2=>\5\6\4\2>?\7\21\2")
        buf.write("\2?|\3\2\2\2@A\7\5\2\2A|\5\6\4\22BC\5\36\20\2CD\5\b\5")
        buf.write("\2DE\5&\24\2E|\3\2\2\2FG\5\36\20\2GH\5\n\6\2HI\5&\24\2")
        buf.write("I|\3\2\2\2JK\5\36\20\2KL\5\f\7\2LM\5&\24\2M|\3\2\2\2N")
        buf.write("O\5\36\20\2OP\5\16\b\2PQ\5&\24\2Q|\3\2\2\2RS\5\36\20\2")
        buf.write("ST\5\20\t\2TU\5&\24\2U|\3\2\2\2VW\5\36\20\2WX\5\20\t\2")
        buf.write("XY\5\34\17\2Y|\3\2\2\2Z[\5\36\20\2[\\\5\22\n\2\\]\5&\24")
        buf.write("\2]|\3\2\2\2^_\5\36\20\2_`\5\22\n\2`a\5\34\17\2a|\3\2")
        buf.write("\2\2bc\5\36\20\2cd\5\24\13\2de\5&\24\2e|\3\2\2\2fg\5\36")
        buf.write("\20\2gh\5\26\f\2hi\5&\24\2ij\5\30\r\2jk\5&\24\2k|\3\2")
        buf.write("\2\2l|\5\36\20\2m|\5&\24\2no\5\36\20\2op\5 \21\2pq\7\20")
        buf.write("\2\2qv\5&\24\2rs\7\25\2\2su\5&\24\2tr\3\2\2\2ux\3\2\2")
        buf.write("\2vt\3\2\2\2vw\3\2\2\2wy\3\2\2\2xv\3\2\2\2yz\7\21\2\2")
        buf.write("z|\3\2\2\2{;\3\2\2\2{@\3\2\2\2{B\3\2\2\2{F\3\2\2\2{J\3")
        buf.write("\2\2\2{N\3\2\2\2{R\3\2\2\2{V\3\2\2\2{Z\3\2\2\2{^\3\2\2")
        buf.write("\2{b\3\2\2\2{f\3\2\2\2{l\3\2\2\2{m\3\2\2\2{n\3\2\2\2|")
        buf.write("\u0087\3\2\2\2}~\f\21\2\2~\177\5\30\r\2\177\u0080\5\6")
        buf.write("\4\22\u0080\u0086\3\2\2\2\u0081\u0082\f\20\2\2\u0082\u0083")
        buf.write("\5\32\16\2\u0083\u0084\5\6\4\21\u0084\u0086\3\2\2\2\u0085")
        buf.write("}\3\2\2\2\u0085\u0081\3\2\2\2\u0086\u0089\3\2\2\2\u0087")
        buf.write("\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088\7\3\2\2\2\u0089")
        buf.write("\u0087\3\2\2\2\u008a\u008b\7\b\2\2\u008b\t\3\2\2\2\u008c")
        buf.write("\u008d\7\t\2\2\u008d\13\3\2\2\2\u008e\u008f\7\n\2\2\u008f")
        buf.write("\r\3\2\2\2\u0090\u0091\7\13\2\2\u0091\17\3\2\2\2\u0092")
        buf.write("\u0093\7\f\2\2\u0093\21\3\2\2\2\u0094\u0095\7\r\2\2\u0095")
        buf.write("\23\3\2\2\2\u0096\u0097\7\16\2\2\u0097\25\3\2\2\2\u0098")
        buf.write("\u0099\7\17\2\2\u0099\27\3\2\2\2\u009a\u009b\7\3\2\2\u009b")
        buf.write("\31\3\2\2\2\u009c\u009d\7\4\2\2\u009d\33\3\2\2\2\u009e")
        buf.write("\u009f\t\2\2\2\u009f\35\3\2\2\2\u00a0\u00a1\7\26\2\2\u00a1")
        buf.write("\37\3\2\2\2\u00a2\u00a3\7\23\2\2\u00a3!\3\2\2\2\u00a4")
        buf.write("\u00a5\7\24\2\2\u00a5#\3\2\2\2\u00a6\u00a7\t\3\2\2\u00a7")
        buf.write("%\3\2\2\2\u00a8\u00ae\5$\23\2\u00a9\u00ae\7\27\2\2\u00aa")
        buf.write("\u00ae\7\30\2\2\u00ab\u00ae\7\36\2\2\u00ac\u00ae\7\37")
        buf.write("\2\2\u00ad\u00a8\3\2\2\2\u00ad\u00a9\3\2\2\2\u00ad\u00aa")
        buf.write("\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ad\u00ac\3\2\2\2\u00ae")
        buf.write("\'\3\2\2\2\u00af\u00b0\7\27\2\2\u00b0)\3\2\2\2\t\609v")
        buf.write("{\u0085\u0087\u00ad")
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
    RULE_limitexpression = 1
    RULE_expression = 2
    RULE_gtComparator = 3
    RULE_geComparator = 4
    RULE_ltComparator = 5
    RULE_leComparator = 6
    RULE_eqComparator = 7
    RULE_neComparator = 8
    RULE_likeComparator = 9
    RULE_betweenComparator = 10
    RULE_andBinary = 11
    RULE_orBinary = 12
    RULE_boolean = 13
    RULE_identifier = 14
    RULE_inOperator = 15
    RULE_limit = 16
    RULE_string = 17
    RULE_value = 18
    RULE_count = 19

    ruleNames =  [ "queryfilter", "limitexpression", "expression", "gtComparator", 
                   "geComparator", "ltComparator", "leComparator", "eqComparator", 
                   "neComparator", "likeComparator", "betweenComparator", 
                   "andBinary", "orBinary", "boolean", "identifier", "inOperator", 
                   "limit", "string", "value", "count" ]

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
        self.checkVersion("4.9.3")
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

        def limitexpression(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.LimitexpressionContext,0)


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
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.expression(0)
                self.state = 41
                self.match(CustomConnectorQueryFilterParser.EOF)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.limitexpression()
                self.state = 44
                self.match(CustomConnectorQueryFilterParser.EOF)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LimitexpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CustomConnectorQueryFilterParser.RULE_limitexpression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LimitExpressionContext(LimitexpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CustomConnectorQueryFilterParser.LimitexpressionContext
            super().__init__(parser)
            self.op = None # LimitContext
            self.right = None # CountContext
            self.left = None # ExpressionContext
            self.copyFrom(ctx)

        def limit(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.LimitContext,0)

        def count(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.CountContext,0)

        def expression(self):
            return self.getTypedRuleContext(CustomConnectorQueryFilterParser.ExpressionContext,0)


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



    def limitexpression(self):

        localctx = CustomConnectorQueryFilterParser.LimitexpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_limitexpression)
        try:
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CustomConnectorQueryFilterParser.LIMIT]:
                localctx = CustomConnectorQueryFilterParser.LimitExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                localctx.op = self.limit()
                self.state = 49
                localctx.right = self.count()
                pass
            elif token in [CustomConnectorQueryFilterParser.NOT, CustomConnectorQueryFilterParser.LPAREN, CustomConnectorQueryFilterParser.NULL, CustomConnectorQueryFilterParser.IDENTIFIER, CustomConnectorQueryFilterParser.POS_INTEGER, CustomConnectorQueryFilterParser.DECIMAL, CustomConnectorQueryFilterParser.SINGLE_STRING, CustomConnectorQueryFilterParser.DOUBLE_STRING, CustomConnectorQueryFilterParser.EMPTY_SINGLE_STRING, CustomConnectorQueryFilterParser.EMPTY_DOUBLE_STRING, CustomConnectorQueryFilterParser.DATE, CustomConnectorQueryFilterParser.DATETIME]:
                localctx = CustomConnectorQueryFilterParser.LimitExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                localctx.left = self.expression(0)
                self.state = 52
                localctx.op = self.limit()
                self.state = 53
                localctx.right = self.count()
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
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = CustomConnectorQueryFilterParser.ParenExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 58
                self.match(CustomConnectorQueryFilterParser.LPAREN)
                self.state = 59
                self.expression(0)
                self.state = 60
                self.match(CustomConnectorQueryFilterParser.RPAREN)
                pass

            elif la_ == 2:
                localctx = CustomConnectorQueryFilterParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 62
                self.match(CustomConnectorQueryFilterParser.NOT)
                self.state = 63
                self.expression(16)
                pass

            elif la_ == 3:
                localctx = CustomConnectorQueryFilterParser.GreaterThanComparatorExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 64
                localctx.left = self.identifier()
                self.state = 65
                localctx.op = self.gtComparator()
                self.state = 66
                localctx.right = self.value()
                pass

            elif la_ == 4:
                localctx = CustomConnectorQueryFilterParser.GreaterThanEqualToComparatorExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 68
                localctx.left = self.identifier()
                self.state = 69
                localctx.op = self.geComparator()
                self.state = 70
                localctx.right = self.value()
                pass

            elif la_ == 5:
                localctx = CustomConnectorQueryFilterParser.LesserThanComparatorExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 72
                localctx.left = self.identifier()
                self.state = 73
                localctx.op = self.ltComparator()
                self.state = 74
                localctx.right = self.value()
                pass

            elif la_ == 6:
                localctx = CustomConnectorQueryFilterParser.LesserThanEqualToComparatorExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 76
                localctx.left = self.identifier()
                self.state = 77
                localctx.op = self.leComparator()
                self.state = 78
                localctx.right = self.value()
                pass

            elif la_ == 7:
                localctx = CustomConnectorQueryFilterParser.EqualToComparatorExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 80
                localctx.left = self.identifier()
                self.state = 81
                localctx.op = self.eqComparator()
                self.state = 82
                localctx.right = self.value()
                pass

            elif la_ == 8:
                localctx = CustomConnectorQueryFilterParser.BooleanEqualToComparatorExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 84
                localctx.left = self.identifier()
                self.state = 85
                localctx.op = self.eqComparator()
                self.state = 86
                localctx.right = self.boolean()
                pass

            elif la_ == 9:
                localctx = CustomConnectorQueryFilterParser.NotEqualToComparatorExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 88
                localctx.left = self.identifier()
                self.state = 89
                localctx.op = self.neComparator()
                self.state = 90
                localctx.right = self.value()
                pass

            elif la_ == 10:
                localctx = CustomConnectorQueryFilterParser.BooleanNotEqualToComparatorExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 92
                localctx.left = self.identifier()
                self.state = 93
                localctx.op = self.neComparator()
                self.state = 94
                localctx.right = self.boolean()
                pass

            elif la_ == 11:
                localctx = CustomConnectorQueryFilterParser.LikeComparatorExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 96
                localctx.left = self.identifier()
                self.state = 97
                localctx.op = self.likeComparator()
                self.state = 98
                localctx.right = self.value()
                pass

            elif la_ == 12:
                localctx = CustomConnectorQueryFilterParser.BetweenExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 100
                localctx.left = self.identifier()
                self.state = 101
                localctx.op = self.betweenComparator()

                self.state = 102
                localctx.l1 = self.value()
                self.state = 103
                localctx.op1 = self.andBinary()
                self.state = 104
                localctx.right = self.value()
                pass

            elif la_ == 13:
                localctx = CustomConnectorQueryFilterParser.IdentifierExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 106
                self.identifier()
                pass

            elif la_ == 14:
                localctx = CustomConnectorQueryFilterParser.ValueExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 107
                self.value()
                pass

            elif la_ == 15:
                localctx = CustomConnectorQueryFilterParser.InExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 108
                self.identifier()
                self.state = 109
                localctx.op = self.inOperator()
                self.state = 110
                self.match(CustomConnectorQueryFilterParser.LPAREN)
                self.state = 111
                self.value()
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CustomConnectorQueryFilterParser.COMMA:
                    self.state = 112
                    self.match(CustomConnectorQueryFilterParser.COMMA)
                    self.state = 113
                    self.value()
                    self.state = 118
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 119
                self.match(CustomConnectorQueryFilterParser.RPAREN)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 133
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 131
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = CustomConnectorQueryFilterParser.ANDBinaryExpressionContext(self, CustomConnectorQueryFilterParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 123
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 124
                        localctx.op = self.andBinary()
                        self.state = 125
                        localctx.right = self.expression(16)
                        pass

                    elif la_ == 2:
                        localctx = CustomConnectorQueryFilterParser.ORBinaryExpressionContext(self, CustomConnectorQueryFilterParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 127
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 128
                        localctx.op = self.orBinary()
                        self.state = 129
                        localctx.right = self.expression(15)
                        pass

             
                self.state = 135
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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
        self.enterRule(localctx, 6, self.RULE_gtComparator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
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
        self.enterRule(localctx, 8, self.RULE_geComparator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
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
        self.enterRule(localctx, 10, self.RULE_ltComparator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
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
        self.enterRule(localctx, 12, self.RULE_leComparator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
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
        self.enterRule(localctx, 14, self.RULE_eqComparator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
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
        self.enterRule(localctx, 16, self.RULE_neComparator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
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
        self.enterRule(localctx, 18, self.RULE_likeComparator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
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
        self.enterRule(localctx, 20, self.RULE_betweenComparator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
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
        self.enterRule(localctx, 22, self.RULE_andBinary)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
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
        self.enterRule(localctx, 24, self.RULE_orBinary)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
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
        self.enterRule(localctx, 26, self.RULE_boolean)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
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
        self.enterRule(localctx, 28, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
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
        self.enterRule(localctx, 30, self.RULE_inOperator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
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
        self.enterRule(localctx, 32, self.RULE_limit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
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
        self.enterRule(localctx, 34, self.RULE_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
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
        self.enterRule(localctx, 36, self.RULE_value)
        try:
            self.state = 171
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CustomConnectorQueryFilterParser.NULL, CustomConnectorQueryFilterParser.SINGLE_STRING, CustomConnectorQueryFilterParser.DOUBLE_STRING, CustomConnectorQueryFilterParser.EMPTY_SINGLE_STRING, CustomConnectorQueryFilterParser.EMPTY_DOUBLE_STRING]:
                localctx = CustomConnectorQueryFilterParser.StringValueExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.string()
                pass
            elif token in [CustomConnectorQueryFilterParser.POS_INTEGER]:
                localctx = CustomConnectorQueryFilterParser.DecimalValueExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.match(CustomConnectorQueryFilterParser.POS_INTEGER)
                pass
            elif token in [CustomConnectorQueryFilterParser.DECIMAL]:
                localctx = CustomConnectorQueryFilterParser.DecimalValueExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 168
                self.match(CustomConnectorQueryFilterParser.DECIMAL)
                pass
            elif token in [CustomConnectorQueryFilterParser.DATE]:
                localctx = CustomConnectorQueryFilterParser.IsoDateContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 169
                self.match(CustomConnectorQueryFilterParser.DATE)
                pass
            elif token in [CustomConnectorQueryFilterParser.DATETIME]:
                localctx = CustomConnectorQueryFilterParser.IsoDateTimeContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 170
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
        self.enterRule(localctx, 38, self.RULE_count)
        try:
            localctx = CustomConnectorQueryFilterParser.CountValueExpressionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 173
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
        self._predicates[2] = self.expression_sempred
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
         




