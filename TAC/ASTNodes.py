class ASTNode:  
    pass  

class Program(ASTNode):  
    def __init__(self, class_declarations):  
        self.class_declarations = class_declarations  

class ClassDeclaration(ASTNode):  
    def __init__(self, name, method_declarations):  
        self.name = name  
        self.method_declarations = method_declarations  

class MethodDeclaration(ASTNode):  
    def __init__(self, name, params, body):  
        self.name = name  
        self.params = params  
        self.body = body  

class VariableDeclaration(ASTNode):  
    def __init__(self, var_type, var_name):  
        self.var_type = var_type  
        self.var_name = var_name  

class Assignment(ASTNode):  
    def __init__(self, var_name, expr):  
        self.var_name = var_name  
        self.expr = expr  

class Expression(ASTNode):  
    def __init__(self, value):  
        self.value = value  

# Additional nodes as necessary...