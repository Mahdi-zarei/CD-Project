import sys
from antlr4 import *
from gen.MyGrammarLexer import MyGrammarLexer
from gen.MyGrammarParser import MyGrammarParser
from MySemanticListener import SemanticAndTACListener
from antlr4.tree.Tree import ParseTreeWalker

def main():
    filename = "./test"
    input_stream = FileStream(filename)
    lexer = MyGrammarLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MyGrammarParser(token_stream)
    tree = parser.goal()

    # Listener for semantic checks and TAC generation
    listener = SemanticAndTACListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    # Output TAC
    print("Three-Address Code (TAC):")
    for line in listener.tac:
        print(line)

if __name__ == "__main__":
    main()