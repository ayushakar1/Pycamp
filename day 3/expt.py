"""
catch error in python
ZeroDivisionError (no divided by 0)
ValueError (wrong value used)
TypeError (eg : str + int)
IndexError (for sets)
IOError (input/output fails) 

"""

try:
    a = int(input("Enter a no:  "))
    print(a*a)
except ValueError:
    print("Please enter a number")

try:
    a = int(input ("Enter a no:"))
    b = int(input ("Enter a no:"))
    print(a/b)
except ZeroDivisionError:
    print("You have entered 0 in second number")  
