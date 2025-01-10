from ASTNodes import *

class TACGenerator:  
    def __init__(self):  
        self.tac = []  
        self.temp_count = 0  

    def new_temp_var(self):  
        temp_var = f"t{self.temp_count}"  
        self.temp_count += 1  
        return temp_var  

    def generate_tac(self, node):  
        if isinstance(node, Program):  
            for class_decl in node.class_declarations:  
                self.generate_tac(class_decl)  

        elif isinstance(node, ClassDeclaration):  
            for method_decl in node.method_declarations:  
                self.generate_tac(method_decl)  

        elif isinstance(node, MethodDeclaration):  
            for var_decl in node.body:  
                self.generate_tac(var_decl)  

        elif isinstance(node, VariableDeclaration):  
            # Assuming we just declare it, we may not need TAC here  
            pass  

        elif isinstance(node, Assignment):  
            temp_var = self.new_temp_var()  
            self.tac.append(f"{temp_var} = {node.expr.value}")  
            self.tac.append(f"{node.var_name} = {temp_var}")  

        elif isinstance(node, Expression):  
            self.tac.append(f"LOAD {node.value}")  

        # Handle additional node types...  

    def get_tac(self):  
        return self.tac