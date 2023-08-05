class Math:
    
    Symbols = ""
    
    Fnumber = 0
    
    Snumber = 0
    
    def __init__(self, Symbols, Fnumber, Snumber):
        
        self.Symbols = Symbols
        
        self.Fnumber = Fnumber
        
        self.Snumber = Snumber
    
    def Addition(self):
        
        # convert str to int
        
        return 
    
    def Minus(self):
        
        return

    def Multipliction(self):
        
        return

    def Division(self):
        
        return
    
    def AllInfo(self):
        
        self.ConvertToInt()
        
        return [self.Fnumber, self.Snumber, self.Symbols]
    
    def ConvertToInt(self):
        
        self.Fnumber = int(self.Fnumber)
        
        self.Snumber = int(self.Snumber)
        
        return 