"""
Rock paper scissor game using conditional statements
"""

import random
computer = random.choice(['rock','paper','scissor'])

 
user = input("Please your choice ---rock paper scissor:")

print("\n Computer Chose:   ",computer)
print(" User Chose: ",user)

print("\n",computer,"V/s",user)

if computer == user:
    print("Match Tied 😅")

elif computer == "rock" and user == "paper":
    print("\n You Win😁")
elif computer == "paper" and user == "scissor":
    print("\n You Win😁")
elif computer == "scissor" and user == "rock":
    print("\n You Win😁")

else:
    print("\n\n You lose😭")