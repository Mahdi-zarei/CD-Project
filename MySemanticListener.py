from gen.MyGrammarListener import MyGrammarListener
from gen.MyGrammarParser import MyGrammarParser
from MySymbolTable import SymbolTable


class SemanticAndTACListener(MyGrammarListener):
    def __init__(self):
        self.staticSemantic = True  # when true, we only scan for members and classes
        self.symbol_table = SymbolTable()
        self.current_class = ''
        self.inFunc = False
        self.temp_counter = 0
        self.expMap = {}

    def defaultForType(self, type_):
        if type_ == 'int[]':
            return "{}"
        if type_ == 'int':
            return "0"
        if type_ == 'boolean':
            return "false"

    def isValidType(self, type_):
        if type_ == 'int' or 'int[]' or 'boolean':
            return True
        if type_ in self.symbol_table.classTables.keys():
            return True
        return False
        
    def get_expr_type(self, expr):
        if isinstance(expr, MyGrammarParser.IdentifierContext):
            return self.symbol_table.lookupVar(expr.getText())
        elif isinstance(expr, MyGrammarParser.NumberExprContext):
            return "int"
        elif isinstance(expr, MyGrammarParser.TrueExprContext) or isinstance(expr, MyGrammarParser.FalseExprContext):
            return "boolean"
        elif isinstance(expr, MyGrammarParser.BinaryExprContext):
            l eft_type = self.get_expr_type(expr.expr(0))
            right_type = self.get_expr_type(expr.expr(1))
            if left_type == right_type:
                    return left_type
            else:
                raise Exception(f"Type mismatch in binary expression: {left_type} and {right_type}")
        return "unknown"

    def exitAssignStat(self, ctx: MyGrammarParser.AssignStatContext):
        var_name = ctx.identifier().getText()
        expr_type = self.get_expr_type(ctx.expr())
        var_type = self.symbol_table.lookupVar(var_name)

        if var_type != expr_type:
            raise Exception(f"Type mismatch: Cannot assign {expr_type} to {var_type}")

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
        self.current_class = ctx.identifier().getText()

    # Exit a parse tree produced by MyGrammarParser#classDeclaration.
    def exitClassDeclaration(self, ctx: MyGrammarParser.ClassDeclarationContext):
        self.symbol_table.exit_scope()
        self.current_class = ''

    # Enter a parse tree produced by MyGrammarParser#varDeclaration.
    def enterVarDeclaration(self, ctx: MyGrammarParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#varDeclaration.
    def exitVarDeclaration(self, ctx: MyGrammarParser.VarDeclarationContext):
        varname = ctx.identifier().getText()
        type_ = ctx.type_().getText()
        if self.current_class != '' and not self.inFunc:
            if not self.staticSemantic:
                # already done
                return
            try:
                self.symbol_table.declareMember(varname, type_, self.current_class)
            except Exception as c:
                print("error in semantic analysis:", c)
                return
        else:
            if self.staticSemantic:
                # incomplete data, ignore
                return
            try:
                if not self.isValidType(type_):
                    raise Exception("unexpected type:", type_)
                self.symbol_table.declareVar(varname, type_)
            except Exception as c:
                print("error in semantic analysis :", c)
                return

    # Enter a parse tree produced by MyGrammarParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx: MyGrammarParser.MethodDeclarationContext):
        self.inFunc = True
        self.symbol_table.enter_scope()
        if self.staticSemantic:
            retType = ctx.type_().getText()
            if self.current_class == '':
                raise Exception("Bad semantic analysis state, cannot declare a method when not in class!")
            self.symbol_table.declareMember(ctx.identifier().getText(), retType, self.current_class)

        inp = ctx.formalList()
        for param in inp:
            if self.staticSemantic:
                try:
                    pType = param.type_().getText()
                    if not self.isValidType(pType):
                        raise Exception("unexpected parameter type:", pType)
                    self.symbol_table.declareMethodParams(self.current_class, ctx.identifier().getText(), pType)
                except Exception as c:
                    print("error in semantic analysis", c)
            else:
                try:
                    pName = param.identifier().getText()
                    pType = param.type_().getText()
                    if not self.isValidType(pType):
                        raise Exception("unexpected parameter type:", pType)
                    self.symbol_table.declareVar(pName, pType)
                except Exception as c:
                    print("error in semantic analysis", c)


    # Exit a parse tree produced by MyGrammarParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx: MyGrammarParser.MethodDeclarationContext):
        self.symbol_table.exit_scope()
        self.inFunc = False

    # Enter a parse tree produced by MyGrammarParser#formalList.
    def enterFormalList(self, ctx: MyGrammarParser.FormalListContext):
        pass

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
        self.symbol_table.enter_scope()

    # Exit a parse tree produced by MyGrammarParser#ifStat.
    def exitIfStat(self, ctx: MyGrammarParser.IfStatContext):
        self.symbol_table.exit_scope()

    # Enter a parse tree produced by MyGrammarParser#whileStat.
    def enterWhileStat(self, ctx: MyGrammarParser.WhileStatContext):
        self.symbol_table.enter_scope()

    # Exit a parse tree produced by MyGrammarParser#whileStat.
    def exitWhileStat(self, ctx: MyGrammarParser.WhileStatContext):
        self.symbol_table.exit_scope()

    # Enter a parse tree produced by MyGrammarParser#printStat.
    def enterPrintStat(self, ctx: MyGrammarParser.PrintStatContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#printStat.
    def exitPrintStat(self, ctx: MyGrammarParser.PrintStatContext):
        pass

    # Enter a parse tree produced by MyGrammarParser#assignStat.
    def enterAssignStat(self, ctx: MyGrammarParser.AssignStatContext):
        pass

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
