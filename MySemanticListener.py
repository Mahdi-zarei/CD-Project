from gen.MyGrammarListener import MyGrammarListener
from gen.MyGrammarParser import MyGrammarParser
from MySymbolTable import SymbolTable


class SemanticAndTACListener(MyGrammarListener):
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.tac = []  # Store TAC instructions
        self.temp_counter = 0
        self.expMap = {}

    def defaultForType(self, type_):
        if type_ == 'int[]':
            return "{}"
        if type_ == 'int':
            return "0"
        if type_ == 'boolean':
            return "false"

    # Enter a parse tree produced by MyGrammarParser#goal.
    def enterGoal(self, ctx: MyGrammarParser.GoalContext):
        self.symbol_table.enter_scope()

    # Exit a parse tree produced by MyGrammarParser#goal.
    def exitGoal(self, ctx: MyGrammarParser.GoalContext):
        self.symbol_table.exit_scope()

    # Enter a parse tree produced by MyGrammarParser#mainClass.
    def enterMainClass(self, ctx: MyGrammarParser.MainClassContext):
        self.symbol_table.enter_scope()

    # Exit a parse tree produced by MyGrammarParser#mainClass.
    def exitMainClass(self, ctx: MyGrammarParser.MainClassContext):
        self.symbol_table.exit_scope()

    # Enter a parse tree produced by MyGrammarParser#classDeclaration.
    def enterClassDeclaration(self, ctx: MyGrammarParser.ClassDeclarationContext):
        self.symbol_table.enter_scope()

    # Exit a parse tree produced by MyGrammarParser#classDeclaration.
    def exitClassDeclaration(self, ctx: MyGrammarParser.ClassDeclarationContext):
        self.symbol_table.exit_scope()

    # Enter a parse tree produced by MyGrammarParser#varDeclaration.
    def enterVarDeclaration(self, ctx: MyGrammarParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#varDeclaration.
    def exitVarDeclaration(self, ctx: MyGrammarParser.VarDeclarationContext):
        varname = ctx.identifier().getText()
        type_ = ctx.type_().getText()
        try:
            print(varname, type_)
            self.symbol_table.declare(varname, type_)
        except Exception as c:
            print("error in semantic analysis :", c)
            return
        self.tac.append(varname + " = " + self.defaultForType(type_) + ";")

    # Enter a parse tree produced by MyGrammarParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx: MyGrammarParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx: MyGrammarParser.MethodDeclarationContext):
        self.symbol_table.exit_scope()

    # Enter a parse tree produced by MyGrammarParser#formalList.
    def enterFormalList(self, ctx: MyGrammarParser.FormalListContext):
        self.symbol_table.enter_scope()

    # Exit a parse tree produced by MyGrammarParser#formalList.
    def exitFormalList(self, ctx: MyGrammarParser.FormalListContext):
        pass

    # Enter a parse tree produced by MyGrammarParser#arrayType.
    def enterArrayType(self, ctx: MyGrammarParser.ArrayTypeContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#arrayType.
    def exitArrayType(self, ctx: MyGrammarParser.ArrayTypeContext):
        pass

    # Enter a parse tree produced by MyGrammarParser#booleanType.
    def enterBooleanType(self, ctx: MyGrammarParser.BooleanTypeContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#booleanType.
    def exitBooleanType(self, ctx: MyGrammarParser.BooleanTypeContext):
        pass

    # Enter a parse tree produced by MyGrammarParser#intType.
    def enterIntType(self, ctx: MyGrammarParser.IntTypeContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#intType.
    def exitIntType(self, ctx: MyGrammarParser.IntTypeContext):
        pass

    # Enter a parse tree produced by MyGrammarParser#idType.
    def enterIdType(self, ctx: MyGrammarParser.IdTypeContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#idType.
    def exitIdType(self, ctx: MyGrammarParser.IdTypeContext):
        pass

    # Enter a parse tree produced by MyGrammarParser#blockStat.
    def enterBlockStat(self, ctx: MyGrammarParser.BlockStatContext):
        self.symbol_table.enter_scope()

    # Exit a parse tree produced by MyGrammarParser#blockStat.
    def exitBlockStat(self, ctx: MyGrammarParser.BlockStatContext):
        self.symbol_table.exit_scope()

    # Enter a parse tree produced by MyGrammarParser#ifStat.
    def enterIfStat(self, ctx: MyGrammarParser.IfStatContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#ifStat.
    def exitIfStat(self, ctx: MyGrammarParser.IfStatContext):
        pass

    # Enter a parse tree produced by MyGrammarParser#whileStat.
    def enterWhileStat(self, ctx: MyGrammarParser.WhileStatContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#whileStat.
    def exitWhileStat(self, ctx: MyGrammarParser.WhileStatContext):
        pass

    # Enter a parse tree produced by MyGrammarParser#printStat.
    def enterPrintStat(self, ctx: MyGrammarParser.PrintStatContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#printStat.
    def exitPrintStat(self, ctx: MyGrammarParser.PrintStatContext):
        pass

    # Enter a parse tree produced by MyGrammarParser#assignStat.
    def enterAssignStat(self, ctx: MyGrammarParser.AssignStatContext):
        varname = ctx.identifier().getText()
        exp = ctx.expression().getText()
        print(varname, exp)

    # Exit a parse tree produced by MyGrammarParser#assignStat.
    def exitAssignStat(self, ctx: MyGrammarParser.AssignStatContext):
        pass

    # Enter a parse tree produced by MyGrammarParser#arrayStat.
    def enterArrayStat(self, ctx: MyGrammarParser.ArrayStatContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#arrayStat.
    def exitArrayStat(self, ctx: MyGrammarParser.ArrayStatContext):
        pass

    # Enter a parse tree produced by MyGrammarParser#newExpr.
    def enterNewExpr(self, ctx: MyGrammarParser.NewExprContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#newExpr.
    def exitNewExpr(self, ctx: MyGrammarParser.NewExprContext):
        pass

    # Enter a parse tree produced by MyGrammarParser#thisExpr.
    def enterThisExpr(self, ctx: MyGrammarParser.ThisExprContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#thisExpr.
    def exitThisExpr(self, ctx: MyGrammarParser.ThisExprContext):
        pass

    # Enter a parse tree produced by MyGrammarParser#arrayExpr.
    def enterArrayExpr(self, ctx: MyGrammarParser.ArrayExprContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#arrayExpr.
    def exitArrayExpr(self, ctx: MyGrammarParser.ArrayExprContext):
        pass

    # Enter a parse tree produced by MyGrammarParser#trueExpr.
    def enterTrueExpr(self, ctx: MyGrammarParser.TrueExprContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#trueExpr.
    def exitTrueExpr(self, ctx: MyGrammarParser.TrueExprContext):
        pass

    # Enter a parse tree produced by MyGrammarParser#numberExpr.
    def enterNumberExpr(self, ctx: MyGrammarParser.NumberExprContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#numberExpr.
    def exitNumberExpr(self, ctx: MyGrammarParser.NumberExprContext):
        pass

    # Enter a parse tree produced by MyGrammarParser#binaryExpr.
    def enterBinaryExpr(self, ctx: MyGrammarParser.BinaryExprContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#binaryExpr.
    def exitBinaryExpr(self, ctx: MyGrammarParser.BinaryExprContext):
        pass

    # Enter a parse tree produced by MyGrammarParser#innerExpr.
    def enterInnerExpr(self, ctx: MyGrammarParser.InnerExprContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#innerExpr.
    def exitInnerExpr(self, ctx: MyGrammarParser.InnerExprContext):
        pass

    # Enter a parse tree produced by MyGrammarParser#newarrayExpr.
    def enterNewarrayExpr(self, ctx: MyGrammarParser.NewarrayExprContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#newarrayExpr.
    def exitNewarrayExpr(self, ctx: MyGrammarParser.NewarrayExprContext):
        pass

    # Enter a parse tree produced by MyGrammarParser#notExpr.
    def enterNotExpr(self, ctx: MyGrammarParser.NotExprContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#notExpr.
    def exitNotExpr(self, ctx: MyGrammarParser.NotExprContext):
        pass

    # Enter a parse tree produced by MyGrammarParser#exprlen.
    def enterExprlen(self, ctx: MyGrammarParser.ExprlenContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#exprlen.
    def exitExprlen(self, ctx: MyGrammarParser.ExprlenContext):
        pass

    # Enter a parse tree produced by MyGrammarParser#falseExpr.
    def enterFalseExpr(self, ctx: MyGrammarParser.FalseExprContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#falseExpr.
    def exitFalseExpr(self, ctx: MyGrammarParser.FalseExprContext):
        pass

    # Enter a parse tree produced by MyGrammarParser#callExpr.
    def enterCallExpr(self, ctx: MyGrammarParser.CallExprContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#callExpr.
    def exitCallExpr(self, ctx: MyGrammarParser.CallExprContext):
        pass

    # Enter a parse tree produced by MyGrammarParser#idExpr.
    def enterIdExpr(self, ctx: MyGrammarParser.IdExprContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#idExpr.
    def exitIdExpr(self, ctx: MyGrammarParser.IdExprContext):
        pass

    # Enter a parse tree produced by MyGrammarParser#identifier.
    def enterIdentifier(self, ctx: MyGrammarParser.IdentifierContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#identifier.
    def exitIdentifier(self, ctx: MyGrammarParser.IdentifierContext):
        pass
