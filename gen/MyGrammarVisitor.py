# Generated from C:/Users/mahdi/PycharmProjects/pythonProject/MyGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MyGrammarParser import MyGrammarParser
else:
    from MyGrammarParser import MyGrammarParser

# This class defines a complete generic visitor for a parse tree produced by MyGrammarParser.

class MyGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyGrammarParser#goal.
    def visitGoal(self, ctx:MyGrammarParser.GoalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#mainClass.
    def visitMainClass(self, ctx:MyGrammarParser.MainClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#classDeclaration.
    def visitClassDeclaration(self, ctx:MyGrammarParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#varDeclaration.
    def visitVarDeclaration(self, ctx:MyGrammarParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:MyGrammarParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#formalList.
    def visitFormalList(self, ctx:MyGrammarParser.FormalListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#arrayType.
    def visitArrayType(self, ctx:MyGrammarParser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#booleanType.
    def visitBooleanType(self, ctx:MyGrammarParser.BooleanTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#intType.
    def visitIntType(self, ctx:MyGrammarParser.IntTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#idType.
    def visitIdType(self, ctx:MyGrammarParser.IdTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#blockStat.
    def visitBlockStat(self, ctx:MyGrammarParser.BlockStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#ifStat.
    def visitIfStat(self, ctx:MyGrammarParser.IfStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#whileStat.
    def visitWhileStat(self, ctx:MyGrammarParser.WhileStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#printStat.
    def visitPrintStat(self, ctx:MyGrammarParser.PrintStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#assignStat.
    def visitAssignStat(self, ctx:MyGrammarParser.AssignStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#arrayStat.
    def visitArrayStat(self, ctx:MyGrammarParser.ArrayStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#newExpr.
    def visitNewExpr(self, ctx:MyGrammarParser.NewExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#thisExpr.
    def visitThisExpr(self, ctx:MyGrammarParser.ThisExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#arrayExpr.
    def visitArrayExpr(self, ctx:MyGrammarParser.ArrayExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#trueExpr.
    def visitTrueExpr(self, ctx:MyGrammarParser.TrueExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#numberExpr.
    def visitNumberExpr(self, ctx:MyGrammarParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#binaryExpr.
    def visitBinaryExpr(self, ctx:MyGrammarParser.BinaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#innerExpr.
    def visitInnerExpr(self, ctx:MyGrammarParser.InnerExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#newarrayExpr.
    def visitNewarrayExpr(self, ctx:MyGrammarParser.NewarrayExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#notExpr.
    def visitNotExpr(self, ctx:MyGrammarParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#exprlen.
    def visitExprlen(self, ctx:MyGrammarParser.ExprlenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#falseExpr.
    def visitFalseExpr(self, ctx:MyGrammarParser.FalseExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#callExpr.
    def visitCallExpr(self, ctx:MyGrammarParser.CallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#idExpr.
    def visitIdExpr(self, ctx:MyGrammarParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#identifier.
    def visitIdentifier(self, ctx:MyGrammarParser.IdentifierContext):
        return self.visitChildren(ctx)



del MyGrammarParser