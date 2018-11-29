#differential functions
import math

import MagicBox

def linear_equation(y_coords, x_coords) -> str:

    gradients = gradient_calculator(y_coords,x_coords,base) 
    """this utilises the gradient_calculator function to calculate the linear gradient"""
    best_fit_grad = round((sum(gradients)/len(gradients)),5) 
    """this rounds the value of the gradient to 5 decimal points, a suitable approximation"""
    y_intercept = y_coords[2]-(best_fit_grad*x_coords[2]) 
    """this calculates the y-intercept via rearrangement of y = mx +c (can utilise any coordinate)"""
    potential_equation = str(best_fit_grad)+"x+"+str(y_intercept) #stores the equation in string format

    return potential_equation

def gradient_calculator(y_coords, x_coords): 
    """stores all of the Y1-Y2/X1-X2 where Y,X represent the lists coordsY and coordsX respectively"""
    gradients = ((y_coords[1:len(y_coords)] - y_coords[0:len(y_coords)-1])
                /(x_coords[1:len(x_coords)] - x_coords[0:len(x_coords)-1]))
                
    return gradients
    """returns all of the values for gradients -> can be further utilised within linear and non-linear equation calculation"""
             
def equation_obtain(y_coords, x_coords, category: str, base: int, repeat_count: int): 
    """the base is the highest power, Category determines which equation function shall be used"""
    
    return_values = []
    obtained_values = [y_coords]
    
    if category == "poly":
    
        while repeat_count != base:
            """this checks if the ammount of recursions is sufficient for the return value to be the correct coefficient (used above)"""
            
            obtained_values.append(gradient_calculator(obtained_values[repeat_count], x_coords))
            repeat_count+=1
        
            coefficient = obtained_values[repeat_count][0]/math.factorial(base) 
            """once the 'base derivative' has been calculated, the value shall be Factorial(Base)*Coefficient"""
            
            x_subtract = MagicBox.Container(list(map(lambda x:(x**base)*coefficient,x_coords))) 
            """Substitutes all X values into the first term"""
            
            y_new = y_coords - x_subtract #First term is subtracted from base Y coordinates
            
            lower_base_term = equation_obtain(y_new,x_coords,"poly",base-1,0) 
            """recursive process is repeated until all coefficients are found"""
            
            if lower_base_term is not None: 
                """checks if the returned values have been obtained (only obtained when correct recursive count is met)"""
                return_values = (lower_base_term)
        
            if gradient_calculator(y_new, x_coords)[0] == 0 and base == 1: 
                """this checks if the previous terms power was 1 and the gradient of the values is 0 (as they should be the same)"""
                
                return_values.append((0,y_new[0]))#Y_new[0] shall be the Y-Intercept in this case
                     
                
                
            return_values.append((base,coefficient)) #adds all of the data about the term to the return values list
            return return_values #returns them for the user
            
def expontential_grad():
    
    exponential_power = [] 
    for i in range(0,len(y_coords)):
        try:
            exponential_power.append(math.log(y_coords[i],x_coords[i]))
        except:
            continue
