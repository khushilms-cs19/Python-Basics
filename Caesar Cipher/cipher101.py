def caesar(direction,message,shift_no):
    final_message=""
    if direction=="encode":
        shift_amount=shift_no
    elif direction=="decode":
        shift_amount=-(shift_no)
    else:
        print("The direction provided is not valid.")
        return 
    for letter in message:
        if letter in symbols:
            final_message+=letter
            continue
        index_of_letter=alphabet.index(letter)
        new_index=(index_of_letter+shift_amount)%26
        final_message+=alphabet[new_index]
    print("The {}d message is: {}".format(direction,final_message))


def clear():
    if name=="nt":
        _ =system("cls")
    else :
        _=system("clear")    



import cipher_art
from os import system, name
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

symbols=''' "#$%&\'()*+,-./:;?@[\\]^_`{|}~1234567890'''
repeat=True
while repeat:
    print(cipher_art.logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction=direction,message=text,shift_no=shift)
    continue_msg=input("Do you want to continue? Type 'yes' or 'no'.\n").lower()
    if continue_msg=="no":
        repeat=False
    clear()    