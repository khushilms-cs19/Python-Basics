print("""
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## We Use the following list as the deck of cards:
##      cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
""")
import random
import art 
from os import system, name
tens=['K','Q','J','10']
suits=["heart","spade","club","diamond"]


def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  random_card=random.choice(cards)
  return random_card


def calculate_score(cards):
  sum_score=0
  for card in cards:
    sum_score+=card
  if len(cards)==2 and sum_score==21:
    return 0
  if sum_score>21:
    if 11 in cards:
      cards.remove(11)
      cards.append(1)
      sum_score-=10  
  return sum_score  


def compare(user_score,computer_score):
    display_all_cards()   
    if user_score==computer_score:
        print("Its a draw")
    elif computer_score==0:
        print("You Lose")
    elif user_score==0:
        print("You Win")
    elif user_score>21:
        print("You Lose")
    elif computer_score>21:
        print("You Win")
    else:
        if user_score>computer_score:
            print("You Win")
        else:
            print("You Lose")


def clear():
    if name=='nt':
        _=system('cls')    
    else:
        _=system('clear')



def get_card_user():
    card_value=deal_card()
    user_cards.append(card_value)
    if card_value==11:
        card_value="A"
    elif card_value==10:
        card_value=random.choice(tens)    
    card_art_key=f"{card_value}{random.choice(suits)}"
    user_cards_art.append(art.each_card[card_art_key])

def get_card_computer():
    card_value=deal_card()
    computer_cards.append(card_value)
    if card_value==11:
        card_value="A"
    elif card_value==10:
        card_value=random.choice(tens)    
    card_art_key=f"{card_value}{random.choice(suits)}"
    computer_cards_art.append(art.each_card[card_art_key])

def display_cards(cards):
    if len(cards)==1:
        print(cards[0])
        return
    for card in cards:
        print(card)

def display_all_cards():
    print("\nComputer final cards: {}".format(computer_cards))
    display_cards(computer_cards_art)
    print("Computer's score: {}\n".format(calculate_score(computer_cards)))
    print("Your final cards: {}".format(user_cards))
    display_cards(user_cards_art)
    print("Your score: {}".format(calculate_score(user_cards)))


play_game=input("Do you want to play blackjack? Type 'y' for yes or 'n' for no :").lower()
if play_game=='y':
  restart=True
else:
  restart=False
user_cards = []
computer_cards = []
user_cards_art=[]
computer_cards_art=[]
card_value=0

while restart:
    clear()

    for i in range(2):
        get_card_user()
    for i in range(2):
        get_card_computer()   
    
    continue_game=True
    while continue_game:
        print(art.logo)
        print("\nComputer cards : {}\n".format(computer_cards[0]))
        display_cards([computer_cards_art[0]])
        print(art.card_behind)
        print("\nYour cards : {}\n".format(user_cards))
        display_cards(user_cards_art)
        print("Your score: {}".format(calculate_score(user_cards)))
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        if user_score==0:
            display_all_cards()
            print("You got a BlackJack!!")
            exit(0)

        if user_score>21:
            display_all_cards()
            print("You lose")
            exit(0)

        another_card=input("Do you want to pick another card? Type 'y' for yes or 'n' for no :").lower()
        if another_card=='y':
            get_card_user()
            clear()
        else:
            continue_game=False

    computer_score=calculate_score(computer_cards)

    while(computer_score<17):
        get_card_computer()
        computer_score=calculate_score(computer_cards)

    clear()
    compare(calculate_score(user_cards),calculate_score(computer_cards))
    play_game=input("Do you want to play another game? Type 'y' for yes or 'n' for no :").lower()
    if play_game=='y':
        restart=True
        clear()
    else:
        restart=False  
