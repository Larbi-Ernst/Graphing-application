#decorators below; these may be used to modify all methods (both special and self-defined) as well as subroutines in the main file


def EquationQuery(Function):

    def Wrapper(self,**kwargs):
        
        if type(self.equation).__name__ == "Equation":
            
            return self.equation
        else:
            
            Function(self,**kwargs)
            
    return Wrapper
        
        
if __name__ == "__main__":
    ValueQuery()

        
            
        
