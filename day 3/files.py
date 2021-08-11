"""
r : reads file
w : Clears entire content of the file and  writes the file
a : appends(adds) contents to the file 
"""

#Reading a file
f = open('demo.txt','r')           #Opens the file/ Creates file pointer     
content = f.read()                 #Reading the content
print(content)                     #Printing the content
f.close()                          #Closing the file

#Writing a file
f = open('demo.txt','w')           #Opens the file/ Creates file pointer     
f.write("New content coming up!!")
f.close()
