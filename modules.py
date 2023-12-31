class Math:
    
    Symbols = ""
    
    Fnumber = 0
    
    Snumber = 0
    
    validSymbols = ["+","-","*","/"]
    
    valid = False
    
    def __init__(self, Symbols, Fnumber, Snumber):
        
        self.Symbols = Symbols
        
        self.Fnumber = Fnumber
        
        self.Snumber = Snumber
    
    def Addition(self):
        
        self.ConvertToInt()
        
        self.Validation()
        
        if self.valid != True:
            
            return "numbers or math symbols is not valid :("
            
        return self.Fnumber + self.Snumber
    
    def Minus(self):
        
        self.ConvertToInt()
        
        self.Validation()
        
        if self.valid != True:
            
            return "numbers or math symbols is not valid :("
            
        return self.Fnumber - self.Snumber

    def Multipliction(self):
        
        self.ConvertToInt()
        
        self.Validation()
        
        if self.valid != True:
            
            return "numbers or math symbols is not valid :("
            
        return self.Fnumber * self.Snumber
        
    def Division(self):
        
        self.ConvertToInt()
        
        self.Validation()
        
        if self.valid != True:
            
            return "numbers or math symbols is not valid :("
            
        return self.Fnumber / self.Snumber
    
    def AllInfo(self):
        
        self.ConvertToInt()
        
        return [self.Fnumber, self.Snumber, self.Symbols]
    
    def ConvertToInt(self):
        
        while self.NumbersValidation() != True:
            
            print("numbers isn't true, enter AGAIN!!!")
            
            self.Fnumber = input("Enter the first number:")
        
            self.Snumber = input("Enter the second number:")
            
            self.NumbersValidation()
            
        self.Fnumber = int(self.Fnumber)
        
        self.Snumber = int(self.Snumber)
        
        return 
    
    def Validation(self):
        
        self.ConvertToInt()
        
        numbersValidation = False
        
        if type(self.Fnumber) and type(self.Snumber) == int:
            
            numbersValidation = True
            
        if self.Symbols in self.validSymbols:
            
            self.valid = True
            
        return self.valid
    
    def NumbersValidation(self):
        
        validation = True
        
        if str(self.Snumber).isdigit() != True or str(self.Fnumber).isdigit() != True:
            
            validation = False
            
        return validation