



no = 0
total = 0.0
 
while True:
    number = input("Enter a number: ")
    if number == 'done':
        break
    try :
        no1 = float(number)
    except:
        print('Invailed Input')
        continue
    no = no+1
    total = total + no1
    
print ("Task Completed Successfully ")
print("\nTotal is ",total)
print("Count is ",no)
 
#print (total,num,total/no)


 