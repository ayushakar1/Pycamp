"""
Define a dictionary for alloting lab subjects according to different day shedule
Given lab1 is alloted for embedded on monday & for TV on tuesday
Lab2 is alloted for 'communication' on Mon & 'antenna' on Tues

Dictionary inside Dictionary 
"""
lab_schedule = {} #empty dictionary
lab_schedule['lab1'] = {}       #empty dictionary for lab 1
lab_schedule['lab2'] = {}       #empty dictionary for lab 2

lab_schedule['lab1']['Mon'] = 'embedded'
lab_schedule['lab1']['Tue'] = 'TV'


lab_schedule['lab2'] ['Mon'] = 'communication'
lab_schedule['lab2'] ['Tue'] = 'antenna'
 
print(lab_schedule)
print(lab_schedule['lab1']['Mon'])
