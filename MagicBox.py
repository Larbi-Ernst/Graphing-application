class Container(list): #this is the data class which shall serve as the data structure used to store graph coordinate data
                  #inherits from list due to the shared functionality; differs in terms of operations however.
    def __new__(self,data):

        self.Accepted_Types = [int,float,complex]
        if any(type(item) not in self.Accepted_Types for item in data): #used to prevent 'incorrect values' for data within the data structure (only allows for numerical values) and no multiple dimensionals
            raise TypeError("expected appropriate type(s) for 'MagicBox.Container': int, float or complex")

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
            raise TypeError("unsupported operand type(s) for *: 'MagicBox.{Self_Type}'".format(Self_Type = self.Self_Type)," and '{Other_Type}'".format(Other_Type = type(other).__name__))

        if any(type(Value) in [list,tuple] for Value in New_Data):
            return tuple((Container(List) for List in New_Data))

        elif all(type(Value) in self.Accepted_Types for Value in New_Data): 
            return Container(New_Data)
    
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

        return Container(New_Data)                         
    
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

        return Container(New_Data)
    
    def __iadd__(self,other):

        New_Data = self + other
        self = New_Data
        return self
    
    def __sub__(self,other):

        if type(other) in self.Accepted_Types:
            New_Data = self + (-1*other)

        elif type(other) == self.Self_Type:
            New_Data = self + Container(list(map(lambda x: -1*x, other)))

        else:
            raise TypeError("unsupported operand type(s) for -: '{Self_Type}'".format(Self_Type = self.Self_Type)+" and '{Other_Type}'".format(Other_Type = type(other).__name__))
            
        return New_Data
    
    def __isub__(self,other):

        New_Data = self - other
        self = New_Data
        return self
    
    def __rmul__(self,other):

        return self.__mul__(other)
