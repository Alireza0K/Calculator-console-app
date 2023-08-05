from modules import Math

print("""
Greeting

Hello there, Welcome to console app Calculator,i know this is a useless app 
but i made it for my self to learn deeply OOP 'Object Oriented Programming'
in below i wrote a Guide note for for you, i describe this for you.

    *ATTENTION* first of all in all option you should to enter numbers and after you can enter your math symbols
    
    1. first option is for Addition, Enter symbols '+' in symbols input.
""")
while True:
    
    AllAndnumbers = list(input().split())

    mathSymbols = AllAndnumbers.append(str(input()))

    math = Math(AllAndnumbers[2], AllAndnumbers[0], AllAndnumbers[1])
    
    if AllAndnumbers[2] not in math.validSymbols:
        
        AllAndnumbers[2] = input("enter another symbol: ")

    if AllAndnumbers[2] == "+":
        
        print(math.Addition())
        
    elif AllAndnumbers[2] == "-":
        
        print(math.Minus())
        
    elif AllAndnumbers[2] == "*":
        
        print(math.Multipliction())
        
    elif AllAndnumbers[2] == "/":
        
        print(math.Division())