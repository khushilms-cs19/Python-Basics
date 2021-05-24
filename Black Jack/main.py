import card_arts
import random
cards=["A","2","3","4","5","6","7","8","9","10","J","Q","K","Joker"]
suits=["heart","spade","diamond","club"]
my_card_list=[]
def get_me_card():
    value=0
    my_card_no=random.choice(cards)
    if my_card_no in ["Q","K","J"]:
        value=10
        my_card_suit=random.choice(suits)
    elif my_card_no=="Joker":
        my_card_suit=""    
    elif my_card_no=="A":
        value=11 
        my_card_suit=random.choice(suits)
    else:
        value=int(my_card_no)  
        my_card_suit=random.choice(suits)
    my_card=my_card_no+my_card_suit
    all_cards=card_arts.each_card
    return all_cards[my_card],value


my_name=input("\nWelcome to the BlackJack Game. Enter your name: ")
print("Hello {}!!".format(my_name))
my_bid=int(input("How much would you like to bet? : $"))
print("So lets get started!!")

my_card_value=0
my_total_money=25000
to_continue=True
print(card_arts.logo)
print(card_arts.dealer_art)
print(card_arts.card_behind)
print(get_me_card())
print("\n\n")
card,value=get_me_card()
my_card_list.append(get_me_card())
my_card_list.append(get_me_card())

while to_continue:
    for card in my_card_list:
        print(card)
        
    print("1:Bet More.\n2:Get A Card.\n3:Drop XD")
    my_choice=input("Enter your option: ")
    if my_choice=="1":
        my_bid+=int(input("How much would you like to add? : "))
    elif my_choice=="2":
        my_card_list.append(get_me_card()) 
    elif my_choice=="3":
        exit()
    




