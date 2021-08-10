"""
set is a collection of unordered elements

"""

list1 = [1,2,30,4,2,6]
print("original = ", list1)
set1 = set(list1)
print(set1)            #ordered and no repeatation

#-------------------------------------


set1 = {2,3,2,3,5}
set2 = {11,2,32,4}
print(set1 | set2)      #union
print(set1 & set2)       #intersection
print(set1 ^ set2)      #elements that are non common

