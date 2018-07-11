import math
global repeat


def linear_gradient(coordsY,coordsX):
    gradients = gradient_calculator(coordsY,coordsX,base,repeat)
    bestFitGrad = round(sum(gradients)/len(gradients),5)
    yIntercept = coordsY[2]-(bestFitGrad*coordsX[2])
    potential_equation = str(bestFitGrad)+"x+"+str(yIntercept)
    print(potential_equation)
    return potential_equation

def gradient_calculator(coordsY,coordsX,repeat):
    #list1,list2 or grad_values
    
    #I'll be using an exponential equation to determine the nature of the curve
    
    gradients = [] #RULE FOR EXPONENTIAL [equation/a^x] won't be negative or have the same y value at 2 points, if negative then odd base, if even y value at 2 points - if negative AND 2 points in same place then sinosodial 
    #start off and linear
    print("NO",coordsY,coordsX)

    for i in range(0,math.floor(len(coordsY))-1):
        gradient = (coordsY[i+1]-coordsY[i])/(coordsX[i+1]-coordsX[i])
        gradients.append(gradient)
    print("YES",gradients)
    return gradients
             
def gradient_obtain(coordsY,coordsX,category,base,repeat):
        
    print("YES")
    Obtained_Values = []
    Obtained_Values.append(coordsY)
    print(Obtained_Values)
    if category == "poly":
        C = 0
        Coefficients = []
            
        if len(Coefficients) == base+1:
            print(Coefficients)
            
        while repeat != base:
            Obtained_Values.append(gradient_calculator(Obtained_Values[repeat],coordsX,repeat))
            repeat+=1
            
           # if (coordsX[0] == 0) and base == 1:
           #C = coordsY[0]
              
           # else:
                #for i in range(len(A)):
                #    C += (coordsY[0]- ((A[i]/base-i)*coordsX[0]**(base-i)))
                
                #Coefficient.append(C)
            
           # print(Coefficient)
              #  for i in coordsY:
               #     newCoordsY = [Coefficient
               # gradient_obtain(Coefficient,coordsX,category = "poly",base+=-1)
            
        #new_coordsY = [
             #  base += -1
            #   print(base)
           #  category = "poly"
            print(Obtained_Values[repeat][0]/math.factorial(base))
            
           
               #if base == 1:
                   #Fact = math.factorial(base)
                  # Coefficient *= Fact
                   #Coefficients.append(Coefficient)
           
                   
               
        
        
       
    #base N
def expontential_grad():
    exponential_power = []
    for i in range(0,len(coordsY)):
        try:
            exponential_power.append(math.log(coordsY[i],coordsX[i]))
        except:
            continue
    print(exponential_power)
    print(sum(exponential_power)/len(exponential_power))
     #exponential    
                
     #a^bx + c find c first

     #regardless of multiplier of X, y-intercept shall be a value which can be determined through Base**A(0) + C - base**A(0)
     #which becomes 1 + C - 1, hence as Base**A(0) becomes 1 + C, we can merely perform Base**A(0) + C - 1 = C
     #A doesn't need to be known as such and we have obtained the base above.

     #now that we found C, we can alter our values such that we have y = a^bx, now we know that we can log2 both sides.

     #log2(y) = log2(x)+log2(b)
     #log2(b) = log2(y) - log2(x)
     #where the base is ((log2(y)-log2(b))/log2(x))

     #Log graph
    
     #n power

     #odd power (one side is negative y, one side is positive y)

     #even power (both are either negative y or positive y)

     #determine rest of equation through x intercept

     #piecewise function in future????

class Data(list):
    def __new__(self,data):
        if type(data) != list or any(type(item) not in [int,float,complex] for item in data): 
            raise TypeError("expected appropriate numerical list data")
        return super().__new__(self,data)
    def __init__(self,data):
        for item in data:
            self.append(item)
            
    def __mul__(self,other):
        return list(map(lambda item: item*other,self))
    
    def __imul__(self,other):
        New_Data = self * (other)
        self = Data(New_Data)
        return self
    
    def __truediv__(self,other):
        return self * (1/other)
    
    def __itruediv__(self,other):
        self *= (1/other)
        return self
    
    
        
 
class Graph:
    def __init__(self,**parameters):
        self.coords = []
        self.equation = ""
        for name,value in parameters.items():
            setattr(self,name,value)
        self.coordsX = Data([coord[0] for coord in self.coords])
        self.coordsY = Data([coord[1] for coord in self.coords])
        
    def get_equation(self,**kwargs):
        for name,value in kwargs.items():
            setattr(self,name,value)
        self.gradient = gradient_obtain(self.coordsY,self.coordsX,self.category,self.base,0)
        print(self.gradient)
        
    def transform(self,ruleX,ruleY):
        print("coords have been mapped")
        
    def set_equation(self,equation):
        self.transform()
        
A = Graph(coords = [(0,5),(1,6),(2,13),(3,32),(4,69),(5,130),(6,(6*36)+5)])
A.get_equation(category = "poly",base = 3)


