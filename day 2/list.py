"""
lists are mutable

"""

shop_list = ["mobile","jeans","grocery","food"]
print(shop_list)
print(shop_list[2])

#----------------Nested list-------------

nlist = [[True,[16]],27,['aayu',9.45]]
print(nlist)

#retrive value from list

print(nlist[0][1])
print(nlist[2])

#--------------------------------

numbers = [2,30,4,53,6,7,56]

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers.append(15)    #append adds the number to last of list
print(numbers)

print(numbers[-2])  #2nd last element

print(numbers[1:4])   #slicing

#--------------------------------------------------

mixed = ["hello","world",True,2.0]
mixed[1]= "ayusha"

print(mixed[:2])       #prints until 2nd index

mixed.insert(2,15)     #insert in a index position
print(mixed)

del mixed[2]       #delets the mentioned index value
print(mixed)