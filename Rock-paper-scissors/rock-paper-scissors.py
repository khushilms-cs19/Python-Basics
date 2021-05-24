import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to rock-paper-scissors challenge.")

my_move=int(input("What do you choose? Type 0 for 'rock', 1 for 'paper', 2 for 'scissors'"))

moves=[rock,paper,scissors]
movesstr=["rock","paper","scissors"]
cpu_move=random.randint(0,1000)
cpu_move=cpu_move%3-1

print("Your move>>>\n")
print(moves[my_move])

print("\n\nComputer's move>>>\n")
print(moves[cpu_move])

cpu_move=movesstr[cpu_move]
my_move=movesstr[my_move]

if my_move=="rock" and cpu_move=="scissors":
  print("\nYou WON!!")
elif my_move=="rock" and cpu_move=="rock":
  print("\nIts a draw.")
elif my_move=="rock" and cpu_move=="paper":
  print("You LOSE!!")
elif my_move=="scissors" and cpu_move=="scissors":
  print("Its a draw")
elif my_move=="scissors" and cpu_move=="rock":
  print("You LOSE!!")
elif my_move=="scissors" and cpu_move=="paper":
  print("You WIN!!")
elif my_move=="paper" and cpu_move=="scissors":
  print("You LOSE!!")
elif my_move=="paper" and cpu_move=="paper":
  print("Its a draw.")
elif my_move=="paper" and cpu_move=="rock":
  print("You WON!!")            