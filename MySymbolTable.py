class SymbolTable:
    def __init__(self):
        self.scopes = [{}]  # Stack of dictionaries for nested scopes, no forward declaration is supported then
        self.classTables = {}  # dictionary to keep the members of a class for object.member type access
        self.methodTable = {}  # dictionary to keep the params of a method. The name of the method will be of form
        # className.methodName and value is a list of types

    def enter_scope(self):
        self.scopes.append({})

    def exit_scope(self):
        self.scopes.pop()

    # no casting is supported, types need to be equal to be valid
    # for class instances, the name of the class will be their type
    def declareVar(self, name, type_):
        if name in self.scopes[-1]:
            raise Exception(f"Variable '{name}' already declared in this scope")
        self.scopes[-1][name] = type_
        print(self.scopes[-1])

    def lookupVar(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        raise Exception(f"Variable '{name}' not declared")

    # we define methods as their return value like int or void
    def declareMember(self, name, type_, className):
        if self.classTables.keys().__contains__(className):
            if self.classTables[className].keys().__contains__(name):
                raise Exception(f"Member '{name}' already declared in this class")
            self.classTables[className][name] = type_
        else:
            self.classTables[className] = {}
            self.classTables[className][name] = type_

    def lookupMember(self, name, className):
        if self.classTables.keys().__contains__(className):
            if self.classTables[className].__contains__(name):
                return self.classTables[className][name]
        raise Exception(f"Member '{name}' not declared")

    def declareMethodParams(self, className, methodName, paramType):
        k = className + '.' + methodName
        if self.methodTable.keys().__contains__(k):
            self.methodTable[k].append(paramType)
        else:
            self.methodTable[k] = []
            self.methodTable[k].append(paramType)

    def lookupMethodParams(self, className, methodName):
        k = className + '.' + methodName
        if not self.methodTable.keys().__contains__(k):
            raise Exception(f"lookup param for unknown method")
        return self.methodTable[k]
