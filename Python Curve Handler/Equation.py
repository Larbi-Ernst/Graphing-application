
        
    
class Equation(object):
            
    def __init__(self):
        self.value = None
        self.operation_order = 0
        self.operations = {"bases":[
            {"coefficient":2,
             "variable":"x",
             "operation_order":0
            }],
              "powers":[]
        }
            
    def __call__(self, variable, other)-> None:
       #value = self.equation.format(x = other)
       #return eval(value)
       print(variable, other)
    
    def __add__(self, other)-> object:
        outcome = Equation()
        outcome.operations["bases"].append((outcome.operation_order,other))
        outcome.operation_order += 1
        return outcome
    
    def __iadd__(self, other)-> object:
        self = self.__add__(self,other)
        return self
    
    def __sub__(self, other)-> object:
        self.__add__(self, -1*other) 
    
    def __isub__(self, other)-> object:
        self.__iadd__(self ,-1*other)
    
    def substitute(self, term, value):
        return None

#Equation -> Terms
        
        
                    

