from ASTNodes import *
from TACGenerator import *

# Sample miniJava AST  
program = Program([  
    ClassDeclaration("Example", [  
        MethodDeclaration("main", [], [  
            VariableDeclaration("int", "x"),  
            Assignment("x", Expression("10"))  
        ])  
    ])  
])  

tac_generator = TACGenerator()  
tac_generator.generate_tac(program)  
tac_code = tac_generator.get_tac()  

# Print the resulting TAC  
print("\n".join(tac_code))