class Container(list): #this is the data class which shall serve as the data structure used to store graph coordinate data
                  #inherits from list due to the shared functionality; differs in terms of operations however.
    def __new__(self,data):

        self.Accepted_Types = [int,float,complex]
        if type(data) != list or any(type(item) not in self.Accepted_Types for item in data): #used to prevent 'incorrect values' for data within the data structure (only allows for numerical values) and no multiple dimensionals
            raise TypeError("expected appropriate type(s) for 'Container': int, float or complex")

        return super().__new__(self,data) #returns a new subtype instance of list
                            
    def __init__(self,data): #initialises the data subclass instance

        for Value in data:
            self.append(Value)
        self.data = data
        
            
    def count_sequences(self,other):

        return count_sequences(self,other)
    
    def lengthen(self,other):

        list_other = list(other) #converts other item into a list for list mutiplication method (data duplication)
        while len(list_other) != len(self) or len(list_other) < len(self): #performs list data duplication until there are an equal or greater count of values within the other data structure than that of the Data
            list_other*=2

        return list_other
    
    def __repr__(self):

        return f'Container({self[:]})'

    def __pow__(self,other):

        New_Data = []
        if type(other) in self.Accepted_Types:
            New_Data = list(map(lambda x:x**other, self))

        elif type(other) == type(self):
            list_other = self.lengthen(other)
            for Index in range(len(self)):
                New_Data.append(self[Index] ** list_other[Index])

        elif type(other) == tuple:
            New_Data = [list(self**Value) for Value in other]

        elif type(other) == dict:
            New_Data = list(self)
            for key,pair in other.items():
                Occurence_List = [Index for Index, Value in enumerate(New_Data) if Value == key]
                for Index in Occurence_List:
                    New_Data[Index] = New_Data[Index]**pair

    def __ipow__(self,other):

        New_Data = self ** other
        self = New_Data
        return self
            
    def __mul__(self,other): #multiplies the values of data by a value and returns new Data

        New_Data = []
        if type(other) in self.Accepted_Types:
            New_Data = list(map(lambda x:x*other, self))
         
        elif type(other) == type(self):
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
            return tuple((Container(List) for List in New_Data))
        
        elif all(type(Value) in self.Accepted_Types for Value in New_Data): 
            return Container(New_Data)
        
    def __imul__(self,other): #performs multiplication method however, returns value as self

        New_Data = self * (other)
        self = New_Data
        return self
    
    def __truediv__(self,other): #performs 'inverse' multiplication method

        if type(other) in self.Accepted_Types:
            New_Data = self * (1/other)
            
        elif type(other) == type(self):
            New_Data = self * Container(list(map(lambda x:1/x,other)))

        elif type(other) == list:
            New_Data = self * list(map(lambda x:1/x,other))

        elif type(other) == tuple:
            New_Data = self * tuple(map(lambda x:1/x,other))

        elif type(other) == dict:
            New_Data = self * dict(map(lambda x: (x[0],1/x[1]),other.items()))
            
        else:
            raise TypeError("unsupported operand type(s) for /: '{Self_Type}'".format(Self_Type = self.Self_Type),"and '{Other_Type}'".format(Other_Type = type(other).__name__))

        return New_Data                        
    
    def __itruediv__(self,other): #performs 'inverse' self-multiplication method

        New_Data = self / (other)
        self = New_Data
        return self
    
    def __add__(self,other): 

        New_Data = []
        if type(other) in self.Accepted_Types:
            New_Data = list(map(lambda x:x+other, self))

        elif type(other) == type(self): #performs Data subtraction method (subtracts each value in Data by that of the corresponding value in Other)
            list_other = self.lengthen(other)
            for i in range(len(self)):
                New_Data.append(self[i] + list_other[i])
                
        elif type(other) == list:
            New_Data = list(self) + other

        elif type(other) == tuple:
            New_Data = [list(map(lambda x:x+other, self)) for Value in other]

        elif type(other) == dict:
            New_Data = list(self)
            for key,pair in other.items():
                Occurence_List = [Index for Index, Value in enumerate(New_Data) if Value == key]
                for Index in Occurence_List:
                    New_Data[Index] = New_Data[Index]+pair
                    
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

        elif type(other) == type(self):
            New_Data = self + Container(list(map(lambda x: -1*x, other)))

        elif type(other) == list:
            for item in other:
                New_Data = list(self).remove(item)

        elif type(other) == tuple:
            New_Data = [list(map(lambda x:x-other, self)) for Value in other]

        elif type(other) == dict:
            New_Data = list(self)
            for key,pair in other.items():
                Occurence_List = [Index for Index, Value in enumerate(New_Data) if Value == key]
                for Index in Occurence_List:
                    New_Data[Index] = New_Data[Index]-pair
            
        else:
            raise TypeError("unsupported operand type(s) for -: '{Self_Type}'".format(Self_Type = self.Self_Type)+" and '{Other_Type}'".format(Other_Type = type(other).__name__))
            
        return New_Data
    
    def __isub__(self,other):

        New_Data = self - other
        self = New_Data
        return self
    
    def __rmul__(self,other):

        return self.__mul__(other)

    def __invert__(self):

        return Container(list(map(lambda x:1/x,self)))

    def __neg__(self):

        return Container(list(map(lambda x:-x,self)))

    def __pos__(self):

        return self

    def __abs__(self):

        return Container(list(map(lambda x:-x if x < 0 else x,self)))

    def polarity(self):

        New_Data = []    
        for item in self:
            try:
                New_Data.append(item/abs(item))
            except:
                New_Data.append(0)
                continue
        return Container(New_Data)
                
                
def count_sequences(main_structure,sequence):
	count = 0
	self_len = len(main_structure)
	other_len = len(sequence)
	print(other_len)
	if self_len-other_len >= 0:
		for index in range(self_len-other_len+1):
			print(main_structure[index:index+other_len])
			if main_structure[index:index+other_len] == sequence:
				count+=1
	return count
