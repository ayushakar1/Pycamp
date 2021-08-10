"""

Write a program to count the number of digits before and after decimal point in the entered floating point number. Take atlease 4
decimal point floating number as input from user

"""

#input 


number =float(input("Enter the number with atleast 4 decimal value: "))
no= number


#after decimal

i=0 
while number != int(number) :
    i = i + 1
    number= number*10

print("Number of digits after decimal= ", i)

#before decimal

j=0
while int(no) != 0 :
    j=j+1
    no= no /10

print("Number of digits before decimal= ",j)