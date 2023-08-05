class Math:
    
    Symbols = ""
    
    Fnumber = 0
    
    Snumber = 0
    
    def __init__(self, Symbols, Fnumber, Snumber):
        
        self.Symbols = Symbols
        
        self.Fnumber = Fnumber
        
        self.Snumber = Snumber
    
    def Addition(self):
        
        return self.AllInfo()
    
    def Minus(self):
        
        return

    def Multipliction(self):
        
        return

    def Division(self):
        
        return
    
    def AllInfo(self):
        
        return [self.Fnumber, self.Snumber, self.Symbols]