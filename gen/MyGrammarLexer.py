# Generated from C:/Users/mahdi/PycharmProjects/pythonProject/MyGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,35,259,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,
        4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,
        8,1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,19,1,19,
        1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,22,
        1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,
        1,25,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,27,1,27,
        1,27,1,27,1,28,1,28,1,29,1,29,5,29,212,8,29,10,29,12,29,215,9,29,
        1,30,4,30,218,8,30,11,30,12,30,219,1,31,1,31,1,31,3,31,225,8,31,
        1,32,4,32,228,8,32,11,32,12,32,229,1,32,1,32,1,33,1,33,1,33,1,33,
        5,33,238,8,33,10,33,12,33,241,9,33,1,33,1,33,1,34,1,34,1,34,1,34,
        1,34,5,34,250,8,34,10,34,12,34,253,9,34,1,34,1,34,1,34,1,34,1,34,
        1,251,0,35,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,
        12,25,13,27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,
        23,47,24,49,25,51,26,53,27,55,28,57,29,59,30,61,31,63,32,65,33,67,
        34,69,35,1,0,6,2,0,65,90,97,122,4,0,48,57,65,90,95,95,97,122,1,0,
        48,57,3,0,42,43,45,45,60,60,3,0,9,10,13,13,32,32,2,0,10,10,13,13,
        265,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,
        0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,
        0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,
        0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,
        0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,
        0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,
        0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,
        1,71,1,0,0,0,3,77,1,0,0,0,5,79,1,0,0,0,7,86,1,0,0,0,9,93,1,0,0,0,
        11,98,1,0,0,0,13,103,1,0,0,0,15,105,1,0,0,0,17,112,1,0,0,0,19,114,
        1,0,0,0,21,116,1,0,0,0,23,118,1,0,0,0,25,120,1,0,0,0,27,122,1,0,
        0,0,29,124,1,0,0,0,31,131,1,0,0,0,33,135,1,0,0,0,35,143,1,0,0,0,
        37,146,1,0,0,0,39,151,1,0,0,0,41,157,1,0,0,0,43,176,1,0,0,0,45,178,
        1,0,0,0,47,180,1,0,0,0,49,187,1,0,0,0,51,192,1,0,0,0,53,198,1,0,
        0,0,55,203,1,0,0,0,57,207,1,0,0,0,59,209,1,0,0,0,61,217,1,0,0,0,
        63,224,1,0,0,0,65,227,1,0,0,0,67,233,1,0,0,0,69,244,1,0,0,0,71,72,
        5,99,0,0,72,73,5,108,0,0,73,74,5,97,0,0,74,75,5,115,0,0,75,76,5,
        115,0,0,76,2,1,0,0,0,77,78,5,123,0,0,78,4,1,0,0,0,79,80,5,112,0,
        0,80,81,5,117,0,0,81,82,5,98,0,0,82,83,5,108,0,0,83,84,5,105,0,0,
        84,85,5,99,0,0,85,6,1,0,0,0,86,87,5,115,0,0,87,88,5,116,0,0,88,89,
        5,97,0,0,89,90,5,116,0,0,90,91,5,105,0,0,91,92,5,99,0,0,92,8,1,0,
        0,0,93,94,5,118,0,0,94,95,5,111,0,0,95,96,5,105,0,0,96,97,5,100,
        0,0,97,10,1,0,0,0,98,99,5,109,0,0,99,100,5,97,0,0,100,101,5,105,
        0,0,101,102,5,110,0,0,102,12,1,0,0,0,103,104,5,40,0,0,104,14,1,0,
        0,0,105,106,5,83,0,0,106,107,5,116,0,0,107,108,5,114,0,0,108,109,
        5,105,0,0,109,110,5,110,0,0,110,111,5,103,0,0,111,16,1,0,0,0,112,
        113,5,91,0,0,113,18,1,0,0,0,114,115,5,93,0,0,115,20,1,0,0,0,116,
        117,5,41,0,0,117,22,1,0,0,0,118,119,5,125,0,0,119,24,1,0,0,0,120,
        121,5,59,0,0,121,26,1,0,0,0,122,123,5,44,0,0,123,28,1,0,0,0,124,
        125,5,114,0,0,125,126,5,101,0,0,126,127,5,116,0,0,127,128,5,117,
        0,0,128,129,5,114,0,0,129,130,5,110,0,0,130,30,1,0,0,0,131,132,5,
        105,0,0,132,133,5,110,0,0,133,134,5,116,0,0,134,32,1,0,0,0,135,136,
        5,98,0,0,136,137,5,111,0,0,137,138,5,111,0,0,138,139,5,108,0,0,139,
        140,5,101,0,0,140,141,5,97,0,0,141,142,5,110,0,0,142,34,1,0,0,0,
        143,144,5,105,0,0,144,145,5,102,0,0,145,36,1,0,0,0,146,147,5,101,
        0,0,147,148,5,108,0,0,148,149,5,115,0,0,149,150,5,101,0,0,150,38,
        1,0,0,0,151,152,5,119,0,0,152,153,5,104,0,0,153,154,5,105,0,0,154,
        155,5,108,0,0,155,156,5,101,0,0,156,40,1,0,0,0,157,158,5,83,0,0,
        158,159,5,121,0,0,159,160,5,115,0,0,160,161,5,116,0,0,161,162,5,
        101,0,0,162,163,5,109,0,0,163,164,5,46,0,0,164,165,5,111,0,0,165,
        166,5,117,0,0,166,167,5,116,0,0,167,168,5,46,0,0,168,169,5,112,0,
        0,169,170,5,114,0,0,170,171,5,105,0,0,171,172,5,110,0,0,172,173,
        5,116,0,0,173,174,5,108,0,0,174,175,5,110,0,0,175,42,1,0,0,0,176,
        177,5,61,0,0,177,44,1,0,0,0,178,179,5,46,0,0,179,46,1,0,0,0,180,
        181,5,108,0,0,181,182,5,101,0,0,182,183,5,110,0,0,183,184,5,103,
        0,0,184,185,5,116,0,0,185,186,5,104,0,0,186,48,1,0,0,0,187,188,5,
        116,0,0,188,189,5,114,0,0,189,190,5,117,0,0,190,191,5,101,0,0,191,
        50,1,0,0,0,192,193,5,102,0,0,193,194,5,97,0,0,194,195,5,108,0,0,
        195,196,5,115,0,0,196,197,5,101,0,0,197,52,1,0,0,0,198,199,5,116,
        0,0,199,200,5,104,0,0,200,201,5,105,0,0,201,202,5,115,0,0,202,54,
        1,0,0,0,203,204,5,110,0,0,204,205,5,101,0,0,205,206,5,119,0,0,206,
        56,1,0,0,0,207,208,5,33,0,0,208,58,1,0,0,0,209,213,7,0,0,0,210,212,
        7,1,0,0,211,210,1,0,0,0,212,215,1,0,0,0,213,211,1,0,0,0,213,214,
        1,0,0,0,214,60,1,0,0,0,215,213,1,0,0,0,216,218,7,2,0,0,217,216,1,
        0,0,0,218,219,1,0,0,0,219,217,1,0,0,0,219,220,1,0,0,0,220,62,1,0,
        0,0,221,222,5,38,0,0,222,225,5,38,0,0,223,225,7,3,0,0,224,221,1,
        0,0,0,224,223,1,0,0,0,225,64,1,0,0,0,226,228,7,4,0,0,227,226,1,0,
        0,0,228,229,1,0,0,0,229,227,1,0,0,0,229,230,1,0,0,0,230,231,1,0,
        0,0,231,232,6,32,0,0,232,66,1,0,0,0,233,234,5,47,0,0,234,235,5,47,
        0,0,235,239,1,0,0,0,236,238,8,5,0,0,237,236,1,0,0,0,238,241,1,0,
        0,0,239,237,1,0,0,0,239,240,1,0,0,0,240,242,1,0,0,0,241,239,1,0,
        0,0,242,243,6,33,1,0,243,68,1,0,0,0,244,245,5,47,0,0,245,246,5,42,
        0,0,246,251,1,0,0,0,247,250,3,69,34,0,248,250,9,0,0,0,249,247,1,
        0,0,0,249,248,1,0,0,0,250,253,1,0,0,0,251,252,1,0,0,0,251,249,1,
        0,0,0,252,254,1,0,0,0,253,251,1,0,0,0,254,255,5,42,0,0,255,256,5,
        47,0,0,256,257,1,0,0,0,257,258,6,34,1,0,258,70,1,0,0,0,8,0,213,219,
        224,229,239,249,251,2,6,0,0,0,1,0
    ]

class MyGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    IDENTIFIER = 30
    INTEGER_LITERAL = 31
    Binary_operators = 32
    WS = 33
    LineComment = 34
    MultiLineComment = 35

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'class'", "'{'", "'public'", "'static'", "'void'", "'main'", 
            "'('", "'String'", "'['", "']'", "')'", "'}'", "';'", "','", 
            "'return'", "'int'", "'boolean'", "'if'", "'else'", "'while'", 
            "'System.out.println'", "'='", "'.'", "'length'", "'true'", 
            "'false'", "'this'", "'new'", "'!'" ]

    symbolicNames = [ "<INVALID>",
            "IDENTIFIER", "INTEGER_LITERAL", "Binary_operators", "WS", "LineComment", 
            "MultiLineComment" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "IDENTIFIER", "INTEGER_LITERAL", 
                  "Binary_operators", "WS", "LineComment", "MultiLineComment" ]

    grammarFileName = "MyGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


