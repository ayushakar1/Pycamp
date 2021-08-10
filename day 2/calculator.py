def add(a,b):
    print( a,"+",b,"=",a+b)

def sub(a,b):
    print("\nSubstraction of",a,"-",b,"=",a-b)

def mul(a,b):
    print("\nProduct of",a,"*",b,"=",a*b)

def div(a,b):
    print("\nDivision of",a,"/",b,"=",a/b)

def pow(a,b):
    print(a,"**",b,"=",a**b)

print("------------------------------------")

print("\n Welcome to my calculator")
print("Available Operations: - \n")
print("1 Addition ")
print("2 Substraction ")
print("3 Multiplication ")
print("4 Division ")
print("5 Power ")

no = float(input("\nPlease Select the operation no - 1/2/3/4/5: "))
if no <  6:     
    
    while True:
        try:
            x = int(input("Enter first no: "))
            y = int(input("Enter second no: "))
            break
        except ValueError:
            print("Oops! Please enter no from 1 to 5...")

print("Wrong input. Please enter no from 1 to 5")

if no == 1:
    add(x,y)
if no == 2:
    sub(x,y)
if no == 3:
    mul(x,y)
if no == 4:
    div(x,y)
if no == 5:
    pow(x,y)

print("---------------------------------------------------")
 
"""function_docstring """