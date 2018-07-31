global repeat
import Control
import Differentiation
import MagicBox


    
class Equation(object):
    
    def __init__(self,equation: list):

        self.equation = equation

    #def __call__(self,other):
       
      # Value = self.str.format(x = other)
       #return eval(Value)
                    
class Graph(object):
    
    def __init__(self,**parameters): #uses keyword argument to pass in all possible parameters, user friendly parameter entry

        self.coords = []
        self.equation = ""
        equation = self.equation
        for name,value in parameters.items():
            setattr(self,name,value) #sets all atributes from parameters
        self.coordsX = MagicBox.Container([coord[0] for coord in self.coords]) #generates Data from subset in coords, this allows the use of the Data operations and methods
        self.coordsY = MagicBox.Container([coord[1] for coord in self.coords])
        
    @Control.EquationQuery
    def get_equation(self,**kwargs): #retrieves the coefficient and power values from the data (best fit equation)
        print("yes")
        for name,value in kwargs.items(): #sets the corresponding keyword argument (in this case it may be type information or base; this shall later be used to speed up the process)
            setattr(self,name,value)

        try:
            self.base #attempts to see if a base value has been provided
        except AttributeError:
            self.base = len(self.coordsX)-1 #utilises best fit 'count of coordinates' to increase the accuracy or provide a possible equation which fits all coords
        print(self.base)
        
            
        self.equation_values = Differentiation.equation_obtain(self.coordsY,self.coordsX,self.category,self.base,0)#returned values of coefficients and coordinates in tuples
        print("Equation:",self.equation_values) 
        self.equation = Equation(self.equation_values)
        print(self.equation.equation)
        
    def transform(self,ruleX,ruleY):

        print("coords have been mapped")
        
    def set_equation(self,equation):

        self.transform()
        
Curve1 = Graph(coords = [(0,5),(1,14),(2,41),(3,98)])#,(4,197),(5,350),(6,569)])
# 2x^3 + 3x^2 + 4x + 5  
Curve1.get_equation(category = "poly",base = 3)


