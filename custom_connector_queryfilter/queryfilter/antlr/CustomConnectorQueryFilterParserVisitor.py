# Generated from CustomConnectorQueryFilterParser.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CustomConnectorQueryFilterParser import CustomConnectorQueryFilterParser
else:
    from CustomConnectorQueryFilterParser import CustomConnectorQueryFilterParser

# This class defines a complete generic visitor for a parse tree produced by CustomConnectorQueryFilterParser.

class CustomConnectorQueryFilterParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CustomConnectorQueryFilterParser#queryfilter.
    def visitQueryfilter(self, ctx:CustomConnectorQueryFilterParser.QueryfilterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#limitExpression.
    def visitLimitExpression(self, ctx:CustomConnectorQueryFilterParser.LimitExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#lesserThanComparatorExpression.
    def visitLesserThanComparatorExpression(self, ctx:CustomConnectorQueryFilterParser.LesserThanComparatorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#greaterThanComparatorExpression.
    def visitGreaterThanComparatorExpression(self, ctx:CustomConnectorQueryFilterParser.GreaterThanComparatorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#booleanEqualToComparatorExpression.
    def visitBooleanEqualToComparatorExpression(self, ctx:CustomConnectorQueryFilterParser.BooleanEqualToComparatorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#valueExpression.
    def visitValueExpression(self, ctx:CustomConnectorQueryFilterParser.ValueExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#booleanNotEqualToComparatorExpression.
    def visitBooleanNotEqualToComparatorExpression(self, ctx:CustomConnectorQueryFilterParser.BooleanNotEqualToComparatorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#identifierExpression.
    def visitIdentifierExpression(self, ctx:CustomConnectorQueryFilterParser.IdentifierExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#notExpression.
    def visitNotExpression(self, ctx:CustomConnectorQueryFilterParser.NotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#parenExpression.
    def visitParenExpression(self, ctx:CustomConnectorQueryFilterParser.ParenExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#oRBinaryExpression.
    def visitORBinaryExpression(self, ctx:CustomConnectorQueryFilterParser.ORBinaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#equalToComparatorExpression.
    def visitEqualToComparatorExpression(self, ctx:CustomConnectorQueryFilterParser.EqualToComparatorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#betweenExpression.
    def visitBetweenExpression(self, ctx:CustomConnectorQueryFilterParser.BetweenExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#inExpression.
    def visitInExpression(self, ctx:CustomConnectorQueryFilterParser.InExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#greaterThanEqualToComparatorExpression.
    def visitGreaterThanEqualToComparatorExpression(self, ctx:CustomConnectorQueryFilterParser.GreaterThanEqualToComparatorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#likeComparatorExpression.
    def visitLikeComparatorExpression(self, ctx:CustomConnectorQueryFilterParser.LikeComparatorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#lesserThanEqualToComparatorExpression.
    def visitLesserThanEqualToComparatorExpression(self, ctx:CustomConnectorQueryFilterParser.LesserThanEqualToComparatorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#notEqualToComparatorExpression.
    def visitNotEqualToComparatorExpression(self, ctx:CustomConnectorQueryFilterParser.NotEqualToComparatorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#aNDBinaryExpression.
    def visitANDBinaryExpression(self, ctx:CustomConnectorQueryFilterParser.ANDBinaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#gtComparator.
    def visitGtComparator(self, ctx:CustomConnectorQueryFilterParser.GtComparatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#geComparator.
    def visitGeComparator(self, ctx:CustomConnectorQueryFilterParser.GeComparatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#ltComparator.
    def visitLtComparator(self, ctx:CustomConnectorQueryFilterParser.LtComparatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#leComparator.
    def visitLeComparator(self, ctx:CustomConnectorQueryFilterParser.LeComparatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#eqComparator.
    def visitEqComparator(self, ctx:CustomConnectorQueryFilterParser.EqComparatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#neComparator.
    def visitNeComparator(self, ctx:CustomConnectorQueryFilterParser.NeComparatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#likeComparator.
    def visitLikeComparator(self, ctx:CustomConnectorQueryFilterParser.LikeComparatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#betweenComparator.
    def visitBetweenComparator(self, ctx:CustomConnectorQueryFilterParser.BetweenComparatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#andBinary.
    def visitAndBinary(self, ctx:CustomConnectorQueryFilterParser.AndBinaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#orBinary.
    def visitOrBinary(self, ctx:CustomConnectorQueryFilterParser.OrBinaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#boolean.
    def visitBoolean(self, ctx:CustomConnectorQueryFilterParser.BooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#identifier.
    def visitIdentifier(self, ctx:CustomConnectorQueryFilterParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#inOperator.
    def visitInOperator(self, ctx:CustomConnectorQueryFilterParser.InOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#limit.
    def visitLimit(self, ctx:CustomConnectorQueryFilterParser.LimitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#string.
    def visitString(self, ctx:CustomConnectorQueryFilterParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#stringValueExpression.
    def visitStringValueExpression(self, ctx:CustomConnectorQueryFilterParser.StringValueExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#decimalValueExpression.
    def visitDecimalValueExpression(self, ctx:CustomConnectorQueryFilterParser.DecimalValueExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#isoDate.
    def visitIsoDate(self, ctx:CustomConnectorQueryFilterParser.IsoDateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#isoDateTime.
    def visitIsoDateTime(self, ctx:CustomConnectorQueryFilterParser.IsoDateTimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CustomConnectorQueryFilterParser#countValueExpression.
    def visitCountValueExpression(self, ctx:CustomConnectorQueryFilterParser.CountValueExpressionContext):
        return self.visitChildren(ctx)



del CustomConnectorQueryFilterParser