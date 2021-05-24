import art
import game_data
import random 
import os
continueGame=True

def clear():

    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
      
currentScore=0
print(art.logo)
valA=random.choice(game_data.data)
print("\nCompare A: {}, a {},from {}.\n".format(valA["name"],valA["description"],valA["country"]))
print(art.vs)
valB=random.choice(game_data.data)

while valA==valB:
    valB=random.choice(game_data.data)

print("Against B: {}, a {}, from {}.".format(valB["name"],valB["description"],valB["country"]))
AorB=input("Who has more followers? Type A or B:").upper()

if valA["follower_count"]>valB["follower_count"] :
    correctAns='A'
else:
    correctAns='B'

if AorB==correctAns:
    continueGame=True
    currentScore+=1
else:
    continueGame=False
valA=valB.copy()
while continueGame:
    clear()
    print(art.logo)
    print("You're right! Current Score: {}".format(currentScore))
    print("\nCompare A: {}, a {},from {}.\n".format(valA["name"],valA["description"],valA["country"]))
    print(art.vs)
    valB=random.choice(game_data.data)

    while valA==valB:
        valB=random.choice(game_data.data)

    print("Against B: {}, a {}, from {}.".format(valB["name"],valB["description"],valB["country"]))
    AorB=input("Who has more followers? Type A or B:").upper()

    if valA["follower_count"]>valB["follower_count"] :
        correctAns='A'
    else:
        correctAns='B'

    if AorB==correctAns:
        continueGame=True
        currentScore+=1
    else:
        continueGame=False

    valA=valB.copy()
    clear()
clear()
print(art.logo)
print("Sorry, that's wrong. Final Score: {}".format(currentScore))