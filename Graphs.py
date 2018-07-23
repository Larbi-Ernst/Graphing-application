import math
global repeat

def linear_equation(coordsY,coordsX):

    gradients = gradient_calculator(coordsY,coordsX,base,repeat) #this utilises the gradient_calculator function to calculate the linear gradient
    bestFitGrad = round(sum(gradients)/len(gradients),5) #this rounds the value of the gradient to 5 decimal points, a suitable approximation
    yIntercept = coordsY[2]-(bestFitGrad*coordsX[2]) #this calculates the y-intercept via rearrangement of y = mx +c (can utilise any coordinate)
    potential_equation = str(bestFitGrad)+"x+"+str(yIntercept) #stores the equation in string format
    print(potential_equation)
    return potential_equation



def gradient_calculator(coordsY,coordsX,repeat):
    
    gradients = [] #stores all of the Y1-Y2/X1-X2 where Y,X represent the lists coordsY and coordsX respectively 
    for i in range(0,math.floor(len(coordsY))-1):
        gradient = (coordsY[i+1]-coordsY[i])/(coordsX[i+1]-coordsX[i])
        gradients.append(gradient)
    return gradients # returns all of the values for gradients -> can be further utilised within linear and non-linear equation calculation
             
def equation_obtain(coordsY,coordsX,category,Base,Repeat_Count): #the base is the highest power, Category determines which equation function shall be used

    Return_Values = []
    Obtained_Values = [coordsY]

    if category == "poly":

        while Repeat_Count != Base:
            Obtained_Values.append(gradient_calculator(Obtained_Values[Repeat_Count],coordsX,Repeat_Count))
            Repeat_Count+=1

            CoefficientFirst = Obtained_Values[Repeat_Count][0]/math.factorial(Base) #once the 'base derivative' has been calculated, the value shall be Factorial(Base)*Coefficient
            X_subtract = MagicBox(list(map(lambda x:(x**Base)*CoefficientFirst,coordsX))) #Substitutes all X values into the first term
            Y_new = coordsY - X_subtract #First term is subtracted from base Y coordinates
            Lower_Base_Value = equation_obtain(Y_new,coordsX,"poly",Base-1,0) #recursive process is repeated until all coefficients are found
            
            if type(Lower_Base_Value) != type(None): #checks if the returned values have been obtained (only obtained when correct recursive count is met)
                Return_Values = (Lower_Base_Value)

            if gradient_calculator(Y_new, coordsX,0)[0] == 0 and Base == 1: #this checks if the previous terms power was 1 and the gradient of the values is 0 (as they should be the same)
                    Return_Values.append((0,Y_new[0]))#Y_new[0] shall be the Y-Intercept in this case
                    
            if Base == Repeat_Count: #this checks if the ammount of recursions is sufficient for the return value to be the correct coefficient (used above)
                Return_Values.append((Base,CoefficientFirst)) #adds all of the data about the term to the return values list
                return Return_Values #returns them for the user
            
def expontential_grad():
    
    exponential_power = [] 
    for i in range(0,len(coordsY)):
        try:
            exponential_power.append(math.log(coordsY[i],coordsX[i]))
        except:
            continue
        
    print(exponential_power)
    print(sum(exponential_power)/len(exponential_power))
class Equation():
    def __init__(self,string):
        self.str = string
        PosNeg = ["-","+"]
        print(A)
    def Plug_In(self,other):
       Value = self.str.format(x = other)
       return eval(Value)
    
                
       
            
            
                
                
        
class MagicBox(list): #this is the data class which shall serve as the data structure used to store graph coordinate data
                  #inherits from list due to the shared functionality; differs in terms of operations however.
    def __new__(self,data):
        self.Accepted_Types = [int,float,complex]
        if any(type(item) not in self.Accepted_Types for item in data): #used to prevent 'incorrect values' for data within the data structure (only allows for numerical values) and no multiple dimensionals
            raise TypeError("expected appropriate type(s) for 'MagicBox': int, float or complex")

        return super().__new__(self,data) #returns a new subtype instance of list
                            
    def __init__(self,data): #initialises the data subclass instance

        self.Self_Type = type(self)
        for Value in data:
            self.append(Value)

    def lengthen(self,other):

        list_other = list(other) #converts other item into a list for list mutiplication method (data duplication)
        while len(list_other) != len(self) or len(list_other) < len(self): #performs list data duplication until there are an equal or greater count of values within the other data structure than that of the Data
            list_other*=2

        return list_other
            
    def __mul__(self,other): #multiplies the values of data by a value and returns new Data

        New_Data = []
        if type(other) in self.Accepted_Types:
            New_Data = list(map(lambda x:x*other, self))
            
        elif type(other) == self.Self_Type:
            list_other = self.lengthen(other)
            for Index in range(len(self)):
                New_Data.append(self[Index] * list_other[Index])

        elif type(other) == list:
            New_Data = [list(self)*Value for Value in other]

        elif type(other) == tuple:
            New_Data = [list(self*Value) for Value in other]

        elif type(other) == dict:
            New_Data = list(self)
            for key,pair in other.items():
                Occurence_List = [Index for Index, Value in enumerate(New_Data) if Value == key]
                for Index in Occurence_List:
                    New_Data[Index] = New_Data[Index]*pair
                    
            
        else:
            raise TypeError("unsupported operand type(s) for *: '{Self_Type}'".format(Self_Type = self.Self_Type)," and '{Other_Type}'".format(Other_Type = type(other).__name__))

        if any(type(Value) in [list,tuple] for Value in New_Data):
            return tuple((MagicBox(List) for List in New_Data))

        elif all(type(Value) in self.Accepted_Types for Value in New_Data): 
            return MagicBox(New_Data)
    
    def __imul__(self,other): #performs multiplication method however, returns value as self

        New_Data = self * (other)
        self = New_Data
        return self
    
    def __truediv__(self,other): #performs 'inverse' multiplication method

        New_Data = []
        if type(other) in self.Accepted_Types:
            New_Data += self * (1/other)
            
        elif type(other) == self.Self_Type:
            New_Data += self * Data(list(map(lambda x:1/x,other)))
            
        else:                                                       
            raise TypeError("unsupported operand type(s) for /: '{Self_Type}'".format(Self_Type = self.Self_Type),"and '{Other_Type}'".format(Other_Type = type(other).__name__))

        return Data(New_Data)                         
    
    def __itruediv__(self,other): #performs 'inverse' self-multiplication method

        New_Data = self / (other)
        self = New_Data
        return self
    
    def __add__(self,other): 

        New_Data = []
        if type(other) in self.Accepted_Types:
            New_Data = list(map(lambda x:x+other, self))

        elif type(other) == self.Self_Type: #performs Data subtraction method (subtracts each value in Data by that of the corresponding value in Other)
            list_other = self.lengthen(other)
            for i in range(len(self)):
                New_Data.append(self[i] + list_other[i])
                
        elif type(other) == list:
            New_Data = list(self) + other
    
        else:
            raise TypeError("unsupported operand type(s) for +: '{Self_Type}'".format(Self_Type = self.Self_Type)," and '{Other_Type}'".format(Other_Type = type(other).__name__))

        return MagicBox(New_Data)
    
    def __iadd__(self,other):

        New_Data = self + other
        self = New_Data
        return self
    
    def __sub__(self,other):

        if type(other) in self.Accepted_Types:
            New_Data = self + (-1*other)

        elif type(other) == self.Self_Type:
            New_Data = self + MagicBox(list(map(lambda x: -1*x, other)))

        else:
            raise TypeError("unsupported operand type(s) for -: '{Self_Type}'".format(Self_Type = self.Self_Type)+" and '{Other_Type}'".format(Other_Type = type(other).__name__))
            
        return New_Data
    
    def __isub__(self,other):

        New_Data = self - other
        self = New_Data
        return self
    
    def __rmul__(self,other):

        return self.__mul__(other)

        
        
        
    
                
class Graph:
    
    def __init__(self,**parameters): #uses keyword argument to pass in all possible parameters, user friendly parameter entry

        self.coords = []
        self.equation = ""
        
        for name,value in parameters.items():
            setattr(self,name,value) #sets all atributes from parameters
        self.coordsX = MagicBox([coord[0] for coord in self.coords]) #generates Data from subset in coords, this allows the use of the Data operations and methods
        self.coordsY = MagicBox([coord[1] for coord in self.coords])
        
    def get_equation(self,**kwargs): #retrieves the coefficient and power values from the data (best fit equation)

        for name,value in kwargs.items(): #sets the corresponding keyword argument (in this case it may be type information or base; this shall later be used to speed up the process)
            setattr(self,name,value)

        try:
            self.base #attempts to see if a base value has been provided
        except AttributeError:
            self.base = len(self.coordsX)-1 #utilises best fit 'count of coordinates' to increase the accuracy or provide a possible equation which fits all coords
        print(self.base)
        
            
        self.equation_values = equation_obtain(self.coordsY,self.coordsX,self.category,self.base,0)#returned values of coefficients and coordinates in tuples
        print("Equation:",self.equation_values) 
        
    def transform(self,ruleX,ruleY):

        print("coords have been mapped")
        
    def set_equation(self,equation):

        self.transform()
        
Curve1 = Graph(coords = [(0,5),(1,14),(2,41),(3,98)])#,(4,197),(5,350),(6,569)])
# 2x^3 + 3x^2 + 4x + 5  
Curve1.get_equation(category = "poly",base = 3)

Curve2 = Graph(coords
