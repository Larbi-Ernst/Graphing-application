
        
    
class Equation(object):
            
    def __init__(self):
        self.value = None
        self.operation_order = 0
        self.operations = {"scaling":[],"shifting":[],"power":[]}
            
    def __call__(self, other):
       value = self.equation.format(x = other)
       return eval(value)

    def __repr__(self):
        return self.operations

    def __add__(self, other):
        outcome = Equation()
        outcome.operations["shifting"].append((outcome.operation_order,other))
        outcome.operation_order += 1
        return outcome

    def __iadd__(self, other):
        self = self.__add__(self,other)
        return self

    def __sub__(self, other):
        self.__add__(self, -1*other) 

    def __isub__(self, other):
        self.__iadd__(self ,-1*other)

    def substitute(self, term, value):
        return None
    
        
        
                    

