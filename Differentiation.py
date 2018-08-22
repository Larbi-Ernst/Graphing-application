#differential functions
import math
import MagicBox
def linear_equation(coordsY, coordsX) -> str:

    gradients = gradient_calculator(coordsY,coordsX,base) 
    """this utilises the gradient_calculator function to calculate the linear gradient"""
    bestFitGrad = round(sum(gradients)/len(gradients),5) 
    """this rounds the value of the gradient to 5 decimal points, a suitable approximation"""
    yIntercept = coordsY[2]-(bestFitGrad*coordsX[2]) 
    """this calculates the y-intercept via rearrangement of y = mx +c (can utilise any coordinate)"""
    potential_equation = str(bestFitGrad)+"x+"+str(yIntercept) #stores the equation in string format
    print(potential_equation)
    return potential_equation



def gradient_calculator(coordsY, coordsX):
    
    gradients = [] 
    """stores all of the Y1-Y2/X1-X2 where Y,X represent the lists coordsY and coordsX respectively"""
  
    for i in range(0,math.floor(len(coordsY))-1):
        gradient = (coordsY[i+1]-coordsY[i])/(coordsX[i+1]-coordsX[i])
        gradients.append(gradient)
    return gradients
    """returns all of the values for gradients -> can be further utilised within linear and non-linear equation calculation"""
             
def equation_obtain(coordsY, coordsX, category: str,Base: int, Repeat_Count: int): 
    """the base is the highest power, Category determines which equation function shall be used"""

    Return_Values = []
    Obtained_Values = [coordsY]

    if category == "poly":

        while Repeat_Count != Base:
            Obtained_Values.append(gradient_calculator(Obtained_Values[Repeat_Count],coordsX))
            Repeat_Count+=1

            CoefficientFirst = Obtained_Values[Repeat_Count][0]/math.factorial(Base) 
            """once the 'base derivative' has been calculated, the value shall be Factorial(Base)*Coefficient"""
            
            X_subtract = MagicBox.Container(list(map(lambda x:(x**Base)*CoefficientFirst,coordsX))) 
            """Substitutes all X values into the first term"""
            
            Y_new = coordsY - X_subtract #First term is subtracted from base Y coordinates
            
            Lower_Base_Value = equation_obtain(Y_new,coordsX,"poly",Base-1,0) 
            """recursive process is repeated until all coefficients are found"""
            
            if Lower_Base_Value is not None: 
                """checks if the returned values have been obtained (only obtained when correct recursive count is met)"""
                Return_Values = (Lower_Base_Value)

            if gradient_calculator(Y_new, coordsX)[0] == 0 and Base == 1: 
                """this checks if the previous terms power was 1 and the gradient of the values is 0 (as they should be the same)"""
                
                Return_Values.append((0,Y_new[0]))#Y_new[0] shall be the Y-Intercept in this case
                    
            if Base == Repeat_Count: 
                """this checks if the ammount of recursions is sufficient for the return value to be the correct coefficient (used above)"""
                
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
