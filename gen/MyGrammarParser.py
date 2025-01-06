# Generated from C:/Users/mahdi/PycharmProjects/pythonProject/MyGrammar.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,36,219,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,5,0,23,8,0,10,0,12,0,26,9,0,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,3,2,52,8,2,1,2,1,2,5,2,56,8,2,10,2,
        12,2,59,9,2,1,2,5,2,62,8,2,10,2,12,2,65,9,2,1,2,1,2,1,3,1,3,1,3,
        1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,80,8,4,10,4,12,4,83,9,4,3,4,
        85,8,4,1,4,1,4,1,4,5,4,90,8,4,10,4,12,4,93,9,4,1,4,5,4,96,8,4,10,
        4,12,4,99,9,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,
        6,1,6,3,6,115,8,6,1,7,1,7,5,7,119,8,7,10,7,12,7,122,9,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        3,7,158,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,183,8,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,
        203,8,8,10,8,12,8,206,9,8,3,8,208,8,8,1,8,1,8,5,8,212,8,8,10,8,12,
        8,215,9,8,1,9,1,9,1,9,0,1,16,10,0,2,4,6,8,10,12,14,16,18,0,0,239,
        0,20,1,0,0,0,2,29,1,0,0,0,4,47,1,0,0,0,6,68,1,0,0,0,8,72,1,0,0,0,
        10,105,1,0,0,0,12,114,1,0,0,0,14,157,1,0,0,0,16,182,1,0,0,0,18,216,
        1,0,0,0,20,24,3,2,1,0,21,23,3,4,2,0,22,21,1,0,0,0,23,26,1,0,0,0,
        24,22,1,0,0,0,24,25,1,0,0,0,25,27,1,0,0,0,26,24,1,0,0,0,27,28,5,
        0,0,1,28,1,1,0,0,0,29,30,5,1,0,0,30,31,3,18,9,0,31,32,5,2,0,0,32,
        33,5,3,0,0,33,34,5,4,0,0,34,35,5,5,0,0,35,36,5,6,0,0,36,37,5,7,0,
        0,37,38,5,8,0,0,38,39,5,9,0,0,39,40,5,10,0,0,40,41,3,18,9,0,41,42,
        5,11,0,0,42,43,5,2,0,0,43,44,3,14,7,0,44,45,5,12,0,0,45,46,5,12,
        0,0,46,3,1,0,0,0,47,48,5,1,0,0,48,51,3,18,9,0,49,50,5,13,0,0,50,
        52,3,18,9,0,51,49,1,0,0,0,51,52,1,0,0,0,52,53,1,0,0,0,53,57,5,2,
        0,0,54,56,3,6,3,0,55,54,1,0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,57,58,
        1,0,0,0,58,63,1,0,0,0,59,57,1,0,0,0,60,62,3,8,4,0,61,60,1,0,0,0,
        62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,66,1,0,0,0,65,63,1,
        0,0,0,66,67,5,12,0,0,67,5,1,0,0,0,68,69,3,12,6,0,69,70,3,18,9,0,
        70,71,5,14,0,0,71,7,1,0,0,0,72,73,5,3,0,0,73,74,3,12,6,0,74,75,3,
        18,9,0,75,84,5,7,0,0,76,81,3,10,5,0,77,78,5,15,0,0,78,80,3,10,5,
        0,79,77,1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,85,
        1,0,0,0,83,81,1,0,0,0,84,76,1,0,0,0,84,85,1,0,0,0,85,86,1,0,0,0,
        86,87,5,11,0,0,87,91,5,2,0,0,88,90,3,6,3,0,89,88,1,0,0,0,90,93,1,
        0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,97,1,0,0,0,93,91,1,0,0,0,94,
        96,3,14,7,0,95,94,1,0,0,0,96,99,1,0,0,0,97,95,1,0,0,0,97,98,1,0,
        0,0,98,100,1,0,0,0,99,97,1,0,0,0,100,101,5,16,0,0,101,102,3,16,8,
        0,102,103,5,14,0,0,103,104,5,12,0,0,104,9,1,0,0,0,105,106,3,12,6,
        0,106,107,3,18,9,0,107,11,1,0,0,0,108,109,5,17,0,0,109,110,5,9,0,
        0,110,115,5,10,0,0,111,115,5,18,0,0,112,115,5,17,0,0,113,115,3,18,
        9,0,114,108,1,0,0,0,114,111,1,0,0,0,114,112,1,0,0,0,114,113,1,0,
        0,0,115,13,1,0,0,0,116,120,5,2,0,0,117,119,3,14,7,0,118,117,1,0,
        0,0,119,122,1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,123,1,0,
        0,0,122,120,1,0,0,0,123,158,5,12,0,0,124,125,5,19,0,0,125,126,5,
        7,0,0,126,127,3,16,8,0,127,128,5,11,0,0,128,129,3,14,7,0,129,130,
        5,20,0,0,130,131,3,14,7,0,131,158,1,0,0,0,132,133,5,21,0,0,133,134,
        5,7,0,0,134,135,3,16,8,0,135,136,5,11,0,0,136,137,3,14,7,0,137,158,
        1,0,0,0,138,139,5,22,0,0,139,140,5,7,0,0,140,141,3,16,8,0,141,142,
        5,11,0,0,142,143,5,14,0,0,143,158,1,0,0,0,144,145,3,18,9,0,145,146,
        5,23,0,0,146,147,3,16,8,0,147,148,5,14,0,0,148,158,1,0,0,0,149,150,
        3,18,9,0,150,151,5,9,0,0,151,152,3,16,8,0,152,153,5,10,0,0,153,154,
        5,23,0,0,154,155,3,16,8,0,155,156,5,14,0,0,156,158,1,0,0,0,157,116,
        1,0,0,0,157,124,1,0,0,0,157,132,1,0,0,0,157,138,1,0,0,0,157,144,
        1,0,0,0,157,149,1,0,0,0,158,15,1,0,0,0,159,160,6,8,-1,0,160,183,
        5,32,0,0,161,183,5,26,0,0,162,183,5,27,0,0,163,183,3,18,9,0,164,
        183,5,28,0,0,165,166,5,29,0,0,166,167,5,17,0,0,167,168,5,9,0,0,168,
        169,3,16,8,0,169,170,5,10,0,0,170,183,1,0,0,0,171,172,5,29,0,0,172,
        173,3,18,9,0,173,174,5,7,0,0,174,175,5,11,0,0,175,183,1,0,0,0,176,
        177,5,30,0,0,177,183,3,16,8,2,178,179,5,7,0,0,179,180,3,16,8,0,180,
        181,5,11,0,0,181,183,1,0,0,0,182,159,1,0,0,0,182,161,1,0,0,0,182,
        162,1,0,0,0,182,163,1,0,0,0,182,164,1,0,0,0,182,165,1,0,0,0,182,
        171,1,0,0,0,182,176,1,0,0,0,182,178,1,0,0,0,183,213,1,0,0,0,184,
        185,10,13,0,0,185,186,5,33,0,0,186,212,3,16,8,14,187,188,10,12,0,
        0,188,189,5,9,0,0,189,190,3,16,8,0,190,191,5,10,0,0,191,212,1,0,
        0,0,192,193,10,11,0,0,193,194,5,24,0,0,194,212,5,25,0,0,195,196,
        10,10,0,0,196,197,5,24,0,0,197,198,3,18,9,0,198,207,5,7,0,0,199,
        204,3,16,8,0,200,201,5,15,0,0,201,203,3,16,8,0,202,200,1,0,0,0,203,
        206,1,0,0,0,204,202,1,0,0,0,204,205,1,0,0,0,205,208,1,0,0,0,206,
        204,1,0,0,0,207,199,1,0,0,0,207,208,1,0,0,0,208,209,1,0,0,0,209,
        210,5,11,0,0,210,212,1,0,0,0,211,184,1,0,0,0,211,187,1,0,0,0,211,
        192,1,0,0,0,211,195,1,0,0,0,212,215,1,0,0,0,213,211,1,0,0,0,213,
        214,1,0,0,0,214,17,1,0,0,0,215,213,1,0,0,0,216,217,5,31,0,0,217,
        19,1,0,0,0,16,24,51,57,63,81,84,91,97,114,120,157,182,204,207,211,
        213
    ]

class MyGrammarParser ( Parser ):

    grammarFileName = "MyGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class'", "'{'", "'public'", "'static'", 
                     "'void'", "'main'", "'('", "'String'", "'['", "']'", 
                     "')'", "'}'", "'extends'", "';'", "','", "'return'", 
                     "'int'", "'boolean'", "'if'", "'else'", "'while'", 
                     "'System.out.println'", "'='", "'.'", "'length'", "'true'", 
                     "'false'", "'this'", "'new'", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "IDENTIFIER", 
                      "INTEGER_LITERAL", "Binary_operators", "WS", "LineComment", 
                      "MultiLineComment" ]

    RULE_goal = 0
    RULE_mainClass = 1
    RULE_classDeclaration = 2
    RULE_varDeclaration = 3
    RULE_methodDeclaration = 4
    RULE_formalList = 5
    RULE_type = 6
    RULE_statement = 7
    RULE_expression = 8
    RULE_identifier = 9

    ruleNames =  [ "goal", "mainClass", "classDeclaration", "varDeclaration", 
                   "methodDeclaration", "formalList", "type", "statement", 
                   "expression", "identifier" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    IDENTIFIER=31
    INTEGER_LITERAL=32
    Binary_operators=33
    WS=34
    LineComment=35
    MultiLineComment=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class GoalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mainClass(self):
            return self.getTypedRuleContext(MyGrammarParser.MainClassContext,0)


        def EOF(self):
            return self.getToken(MyGrammarParser.EOF, 0)

        def classDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.ClassDeclarationContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.ClassDeclarationContext,i)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_goal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGoal" ):
                listener.enterGoal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGoal" ):
                listener.exitGoal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGoal" ):
                return visitor.visitGoal(self)
            else:
                return visitor.visitChildren(self)




    def goal(self):

        localctx = MyGrammarParser.GoalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_goal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.mainClass()
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 21
                self.classDeclaration()
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 27
            self.match(MyGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainClassContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.IdentifierContext,i)


        def statement(self):
            return self.getTypedRuleContext(MyGrammarParser.StatementContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_mainClass

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMainClass" ):
                listener.enterMainClass(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMainClass" ):
                listener.exitMainClass(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMainClass" ):
                return visitor.visitMainClass(self)
            else:
                return visitor.visitChildren(self)




    def mainClass(self):

        localctx = MyGrammarParser.MainClassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mainClass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(MyGrammarParser.T__0)
            self.state = 30
            self.identifier()
            self.state = 31
            self.match(MyGrammarParser.T__1)
            self.state = 32
            self.match(MyGrammarParser.T__2)
            self.state = 33
            self.match(MyGrammarParser.T__3)
            self.state = 34
            self.match(MyGrammarParser.T__4)
            self.state = 35
            self.match(MyGrammarParser.T__5)
            self.state = 36
            self.match(MyGrammarParser.T__6)
            self.state = 37
            self.match(MyGrammarParser.T__7)
            self.state = 38
            self.match(MyGrammarParser.T__8)
            self.state = 39
            self.match(MyGrammarParser.T__9)
            self.state = 40
            self.identifier()
            self.state = 41
            self.match(MyGrammarParser.T__10)
            self.state = 42
            self.match(MyGrammarParser.T__1)
            self.state = 43
            self.statement()
            self.state = 44
            self.match(MyGrammarParser.T__11)
            self.state = 45
            self.match(MyGrammarParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.IdentifierContext,i)


        def varDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.VarDeclarationContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.VarDeclarationContext,i)


        def methodDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.MethodDeclarationContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.MethodDeclarationContext,i)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_classDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDeclaration" ):
                listener.enterClassDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDeclaration" ):
                listener.exitClassDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDeclaration" ):
                return visitor.visitClassDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def classDeclaration(self):

        localctx = MyGrammarParser.ClassDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(MyGrammarParser.T__0)
            self.state = 48
            self.identifier()
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 49
                self.match(MyGrammarParser.T__12)
                self.state = 50
                self.identifier()


            self.state = 53
            self.match(MyGrammarParser.T__1)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2147876864) != 0):
                self.state = 54
                self.varDeclaration()
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 60
                self.methodDeclaration()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
            self.match(MyGrammarParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(MyGrammarParser.TypeContext,0)


        def identifier(self):
            return self.getTypedRuleContext(MyGrammarParser.IdentifierContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_varDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDeclaration" ):
                listener.enterVarDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDeclaration" ):
                listener.exitVarDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclaration" ):
                return visitor.visitVarDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def varDeclaration(self):

        localctx = MyGrammarParser.VarDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_varDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.type_()
            self.state = 69
            self.identifier()
            self.state = 70
            self.match(MyGrammarParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(MyGrammarParser.TypeContext,0)


        def identifier(self):
            return self.getTypedRuleContext(MyGrammarParser.IdentifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(MyGrammarParser.ExpressionContext,0)


        def formalList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.FormalListContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.FormalListContext,i)


        def varDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.VarDeclarationContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.VarDeclarationContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_methodDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodDeclaration" ):
                listener.enterMethodDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodDeclaration" ):
                listener.exitMethodDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDeclaration" ):
                return visitor.visitMethodDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def methodDeclaration(self):

        localctx = MyGrammarParser.MethodDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_methodDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(MyGrammarParser.T__2)
            self.state = 73
            self.type_()
            self.state = 74
            self.identifier()
            self.state = 75
            self.match(MyGrammarParser.T__6)
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2147876864) != 0):
                self.state = 76
                self.formalList()
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 77
                    self.match(MyGrammarParser.T__14)
                    self.state = 78
                    self.formalList()
                    self.state = 83
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 86
            self.match(MyGrammarParser.T__10)
            self.state = 87
            self.match(MyGrammarParser.T__1)
            self.state = 91
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 88
                    self.varDeclaration() 
                self.state = 93
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2154299396) != 0):
                self.state = 94
                self.statement()
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 100
            self.match(MyGrammarParser.T__15)
            self.state = 101
            self.expression(0)
            self.state = 102
            self.match(MyGrammarParser.T__13)
            self.state = 103
            self.match(MyGrammarParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormalListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(MyGrammarParser.TypeContext,0)


        def identifier(self):
            return self.getTypedRuleContext(MyGrammarParser.IdentifierContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_formalList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormalList" ):
                listener.enterFormalList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormalList" ):
                listener.exitFormalList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormalList" ):
                return visitor.visitFormalList(self)
            else:
                return visitor.visitChildren(self)




    def formalList(self):

        localctx = MyGrammarParser.FormalListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_formalList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.type_()
            self.state = 106
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyGrammarParser.RULE_type

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ArrayTypeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayType" ):
                listener.enterArrayType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayType" ):
                listener.exitArrayType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayType" ):
                return visitor.visitArrayType(self)
            else:
                return visitor.visitChildren(self)


    class BooleanTypeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanType" ):
                listener.enterBooleanType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanType" ):
                listener.exitBooleanType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanType" ):
                return visitor.visitBooleanType(self)
            else:
                return visitor.visitChildren(self)


    class IdTypeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(MyGrammarParser.IdentifierContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdType" ):
                listener.enterIdType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdType" ):
                listener.exitIdType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdType" ):
                return visitor.visitIdType(self)
            else:
                return visitor.visitChildren(self)


    class IntTypeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntType" ):
                listener.enterIntType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntType" ):
                listener.exitIntType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntType" ):
                return visitor.visitIntType(self)
            else:
                return visitor.visitChildren(self)



    def type_(self):

        localctx = MyGrammarParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_type)
        try:
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = MyGrammarParser.ArrayTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.match(MyGrammarParser.T__16)
                self.state = 109
                self.match(MyGrammarParser.T__8)
                self.state = 110
                self.match(MyGrammarParser.T__9)
                pass

            elif la_ == 2:
                localctx = MyGrammarParser.BooleanTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                self.match(MyGrammarParser.T__17)
                pass

            elif la_ == 3:
                localctx = MyGrammarParser.IntTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 112
                self.match(MyGrammarParser.T__16)
                pass

            elif la_ == 4:
                localctx = MyGrammarParser.IdTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 113
                self.identifier()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyGrammarParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IfStatContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(MyGrammarParser.ExpressionContext,0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStat" ):
                listener.enterIfStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStat" ):
                listener.exitIfStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStat" ):
                return visitor.visitIfStat(self)
            else:
                return visitor.visitChildren(self)


    class BlockStatContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockStat" ):
                listener.enterBlockStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockStat" ):
                listener.exitBlockStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStat" ):
                return visitor.visitBlockStat(self)
            else:
                return visitor.visitChildren(self)


    class PrintStatContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(MyGrammarParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStat" ):
                listener.enterPrintStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStat" ):
                listener.exitPrintStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStat" ):
                return visitor.visitPrintStat(self)
            else:
                return visitor.visitChildren(self)


    class AssignStatContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(MyGrammarParser.IdentifierContext,0)

        def expression(self):
            return self.getTypedRuleContext(MyGrammarParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStat" ):
                listener.enterAssignStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStat" ):
                listener.exitAssignStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStat" ):
                return visitor.visitAssignStat(self)
            else:
                return visitor.visitChildren(self)


    class ArrayStatContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(MyGrammarParser.IdentifierContext,0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayStat" ):
                listener.enterArrayStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayStat" ):
                listener.exitArrayStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayStat" ):
                return visitor.visitArrayStat(self)
            else:
                return visitor.visitChildren(self)


    class WhileStatContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(MyGrammarParser.ExpressionContext,0)

        def statement(self):
            return self.getTypedRuleContext(MyGrammarParser.StatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStat" ):
                listener.enterWhileStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStat" ):
                listener.exitWhileStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStat" ):
                return visitor.visitWhileStat(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = MyGrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = MyGrammarParser.BlockStatContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.match(MyGrammarParser.T__1)
                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2154299396) != 0):
                    self.state = 117
                    self.statement()
                    self.state = 122
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 123
                self.match(MyGrammarParser.T__11)
                pass

            elif la_ == 2:
                localctx = MyGrammarParser.IfStatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.match(MyGrammarParser.T__18)
                self.state = 125
                self.match(MyGrammarParser.T__6)
                self.state = 126
                self.expression(0)
                self.state = 127
                self.match(MyGrammarParser.T__10)
                self.state = 128
                self.statement()
                self.state = 129
                self.match(MyGrammarParser.T__19)
                self.state = 130
                self.statement()
                pass

            elif la_ == 3:
                localctx = MyGrammarParser.WhileStatContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 132
                self.match(MyGrammarParser.T__20)
                self.state = 133
                self.match(MyGrammarParser.T__6)
                self.state = 134
                self.expression(0)
                self.state = 135
                self.match(MyGrammarParser.T__10)
                self.state = 136
                self.statement()
                pass

            elif la_ == 4:
                localctx = MyGrammarParser.PrintStatContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 138
                self.match(MyGrammarParser.T__21)
                self.state = 139
                self.match(MyGrammarParser.T__6)
                self.state = 140
                self.expression(0)
                self.state = 141
                self.match(MyGrammarParser.T__10)
                self.state = 142
                self.match(MyGrammarParser.T__13)
                pass

            elif la_ == 5:
                localctx = MyGrammarParser.AssignStatContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 144
                self.identifier()
                self.state = 145
                self.match(MyGrammarParser.T__22)
                self.state = 146
                self.expression(0)
                self.state = 147
                self.match(MyGrammarParser.T__13)
                pass

            elif la_ == 6:
                localctx = MyGrammarParser.ArrayStatContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 149
                self.identifier()
                self.state = 150
                self.match(MyGrammarParser.T__8)
                self.state = 151
                self.expression(0)
                self.state = 152
                self.match(MyGrammarParser.T__9)
                self.state = 153
                self.match(MyGrammarParser.T__22)
                self.state = 154
                self.expression(0)
                self.state = 155
                self.match(MyGrammarParser.T__13)
                pass


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
            return MyGrammarParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NewExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(MyGrammarParser.IdentifierContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNewExpr" ):
                listener.enterNewExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNewExpr" ):
                listener.exitNewExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewExpr" ):
                return visitor.visitNewExpr(self)
            else:
                return visitor.visitChildren(self)


    class ThisExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThisExpr" ):
                listener.enterThisExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThisExpr" ):
                listener.exitThisExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThisExpr" ):
                return visitor.visitThisExpr(self)
            else:
                return visitor.visitChildren(self)


    class ArrayExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayExpr" ):
                listener.enterArrayExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayExpr" ):
                listener.exitArrayExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayExpr" ):
                return visitor.visitArrayExpr(self)
            else:
                return visitor.visitChildren(self)


    class TrueExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrueExpr" ):
                listener.enterTrueExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrueExpr" ):
                listener.exitTrueExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrueExpr" ):
                return visitor.visitTrueExpr(self)
            else:
                return visitor.visitChildren(self)


    class NumberExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(MyGrammarParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpr" ):
                return visitor.visitNumberExpr(self)
            else:
                return visitor.visitChildren(self)


    class BinaryExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.ExpressionContext,i)

        def Binary_operators(self):
            return self.getToken(MyGrammarParser.Binary_operators, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryExpr" ):
                listener.enterBinaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryExpr" ):
                listener.exitBinaryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryExpr" ):
                return visitor.visitBinaryExpr(self)
            else:
                return visitor.visitChildren(self)


    class InnerExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(MyGrammarParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInnerExpr" ):
                listener.enterInnerExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInnerExpr" ):
                listener.exitInnerExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInnerExpr" ):
                return visitor.visitInnerExpr(self)
            else:
                return visitor.visitChildren(self)


    class NewarrayExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(MyGrammarParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNewarrayExpr" ):
                listener.enterNewarrayExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNewarrayExpr" ):
                listener.exitNewarrayExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewarrayExpr" ):
                return visitor.visitNewarrayExpr(self)
            else:
                return visitor.visitChildren(self)


    class NotExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(MyGrammarParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpr" ):
                listener.enterNotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpr" ):
                listener.exitNotExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)


    class ExprlenContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(MyGrammarParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprlen" ):
                listener.enterExprlen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprlen" ):
                listener.exitExprlen(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlen" ):
                return visitor.visitExprlen(self)
            else:
                return visitor.visitChildren(self)


    class FalseExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFalseExpr" ):
                listener.enterFalseExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFalseExpr" ):
                listener.exitFalseExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFalseExpr" ):
                return visitor.visitFalseExpr(self)
            else:
                return visitor.visitChildren(self)


    class CallExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.ExpressionContext,i)

        def identifier(self):
            return self.getTypedRuleContext(MyGrammarParser.IdentifierContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallExpr" ):
                listener.enterCallExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallExpr" ):
                listener.exitCallExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallExpr" ):
                return visitor.visitCallExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(MyGrammarParser.IdentifierContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExpr" ):
                listener.enterIdExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExpr" ):
                listener.exitIdExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdExpr" ):
                return visitor.visitIdExpr(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyGrammarParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                localctx = MyGrammarParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 160
                self.match(MyGrammarParser.INTEGER_LITERAL)
                pass

            elif la_ == 2:
                localctx = MyGrammarParser.TrueExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 161
                self.match(MyGrammarParser.T__25)
                pass

            elif la_ == 3:
                localctx = MyGrammarParser.FalseExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 162
                self.match(MyGrammarParser.T__26)
                pass

            elif la_ == 4:
                localctx = MyGrammarParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 163
                self.identifier()
                pass

            elif la_ == 5:
                localctx = MyGrammarParser.ThisExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 164
                self.match(MyGrammarParser.T__27)
                pass

            elif la_ == 6:
                localctx = MyGrammarParser.NewarrayExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 165
                self.match(MyGrammarParser.T__28)
                self.state = 166
                self.match(MyGrammarParser.T__16)
                self.state = 167
                self.match(MyGrammarParser.T__8)
                self.state = 168
                self.expression(0)
                self.state = 169
                self.match(MyGrammarParser.T__9)
                pass

            elif la_ == 7:
                localctx = MyGrammarParser.NewExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 171
                self.match(MyGrammarParser.T__28)
                self.state = 172
                self.identifier()
                self.state = 173
                self.match(MyGrammarParser.T__6)
                self.state = 174
                self.match(MyGrammarParser.T__10)
                pass

            elif la_ == 8:
                localctx = MyGrammarParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 176
                self.match(MyGrammarParser.T__29)
                self.state = 177
                self.expression(2)
                pass

            elif la_ == 9:
                localctx = MyGrammarParser.InnerExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 178
                self.match(MyGrammarParser.T__6)
                self.state = 179
                self.expression(0)
                self.state = 180
                self.match(MyGrammarParser.T__10)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 213
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 211
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = MyGrammarParser.BinaryExprContext(self, MyGrammarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 184
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 185
                        self.match(MyGrammarParser.Binary_operators)
                        self.state = 186
                        self.expression(14)
                        pass

                    elif la_ == 2:
                        localctx = MyGrammarParser.ArrayExprContext(self, MyGrammarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 187
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 188
                        self.match(MyGrammarParser.T__8)
                        self.state = 189
                        self.expression(0)
                        self.state = 190
                        self.match(MyGrammarParser.T__9)
                        pass

                    elif la_ == 3:
                        localctx = MyGrammarParser.ExprlenContext(self, MyGrammarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 192
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 193
                        self.match(MyGrammarParser.T__23)
                        self.state = 194
                        self.match(MyGrammarParser.T__24)
                        pass

                    elif la_ == 4:
                        localctx = MyGrammarParser.CallExprContext(self, MyGrammarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 195
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 196
                        self.match(MyGrammarParser.T__23)
                        self.state = 197
                        self.identifier()
                        self.state = 198
                        self.match(MyGrammarParser.T__6)
                        self.state = 207
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8522825856) != 0):
                            self.state = 199
                            self.expression(0)
                            self.state = 204
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==15:
                                self.state = 200
                                self.match(MyGrammarParser.T__14)
                                self.state = 201
                                self.expression(0)
                                self.state = 206
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)



                        self.state = 209
                        self.match(MyGrammarParser.T__10)
                        pass

             
                self.state = 215
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MyGrammarParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_identifier

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

        localctx = MyGrammarParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(MyGrammarParser.IDENTIFIER)
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
        self._predicates[8] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 10)
         




