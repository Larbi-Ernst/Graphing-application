#decorators below; these may be used to modify all methods (both special and self-defined) as well as subroutines in the main file


def equation_query(func):

    def wrapper(self,**kwargs):
      
        if type(self.equation).__name__ == "Equation":
            return self.equation
        else:
            func(self,**kwargs)
            
    return wrapper
        
        
if __name__ == "__main__":
    equation_query()

        
            
        
