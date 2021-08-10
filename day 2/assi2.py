print("--------------------------")
print("\n Select any one case")
print("\n 1. print single quote \n 2. print comma \n 3. print colon \n 4. print double quotes \n 5. print fullstop \n 6. print slash \n 7. print back slash \n 8. print exclaimation mark \n 9. print semicolon")

ch = int(input("Enter choice: "))

if(ch>9):
    print("You gave a wrong choice")
else:
    if(ch==1):
        print("'")
    if(ch==2):
        print(",")
    if(ch==3):
        print(":")
    if(ch==4):
        print('"')
    if(ch==5):
        print(".")
    if(ch==6):
        print("/")
    if(ch==7):
        print("\\")
    if(ch==8):
        print("!")
    if(ch==9):
        print(";")                                

print("-----------------------------------------------")
