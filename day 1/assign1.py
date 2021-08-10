"""
Question 1 ( Write a program to take input from user for shopping amount. For amount, greater than 1000 shopkeeper gives 10 percent discount
and for amount below 1000 he gives 5 percent discount. Write a program to display percent discount and amount of discount applicable)


"""

amount = int(input("Enter the shopping amount: "))

#checking by condition

if amount>=1000 :
    print("You get 10 percent discount!")
    print("Your discount amount= ",0.1*amount)
else :
    print("You get 5 percent discount!")
    print("Your discount amount=", 0.05*amount)    
