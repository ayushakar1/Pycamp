list()
i=0
total=0

while input != "done" :
    list(i)= input("Enter number: ")
    total= total + list(i)
    i=i+1

print("entry is taken")
print(total,i,max(list),min(list))

