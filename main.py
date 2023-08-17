from modules import Math

print("""
Greeting

Hello there, Welcome to console app Calculator,i know this is a useless app 
but i made it for my self to learn deeply OOP 'Object Oriented Programming'
in below i wrote a Guide note for you, i describe this for you.

    *ATTENTION* first of all in all option you should to enter numbers and after you can enter your math symbols
    
    1. first option is for Addition, Enter symbols '+' in symbols input.
    2. second option is for Minus, Enter symbols '-' in symbols input.
    3. third option is for Multipliction, Enter symbols '*' in symbols input.
    4. fourth option is for Division, Enter symbols '/' in symbols input.
""")

under = "<==========*|*==========>"

while True:
    
    AllAndnumbers = list(input("Enter the numbers with a gap between: ").split())

    mathSymbols = AllAndnumbers.append(str(input("Enter the math symbol you want:")))
    
    if len(AllAndnumbers) != 3: # validation, it's forced user to enter whole inputs.

        print("you didn't enter some of inputs try again")
        
        continue
        
    math = Math(AllAndnumbers[2], AllAndnumbers[0], AllAndnumbers[1])
    
    while AllAndnumbers[2] not in math.validSymbols:
        
        AllAndnumbers[2] = input("enter another symbol: ")
        
    math = Math(AllAndnumbers[2], AllAndnumbers[0], AllAndnumbers[1])

    if AllAndnumbers[2] == "+":
        
        print(math.Addition())
        
        print(under)
        
    elif AllAndnumbers[2] == "-":
        
        print(math.Minus())
    
        print(under)
        
    elif AllAndnumbers[2] == "*":
        
        print(math.Multipliction())
        
        print(under)
        
    elif AllAndnumbers[2] == "/":
        
        print(math.Division())
        
        print(under)