
import random

import hangman_words

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


import hangman_art
print(hangman_art.logo)

# print(f'the solution is {chosen_word}.')


display = []
for _ in range(word_length):
    display += "_"
guessed_letters=[]
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
      print("You have already guessed the letter '{}' .".format(guess))
    else:
      guessed_letters.append(guess)  
 
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter


    if guess not in chosen_word:
        print("The letter you guessed '{}', is not in the word.".format(guess))
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(hangman_art.you_lose)
            print("The solution was: {}".format(chosen_word))

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print(hangman_art.you_win)
    print(hangman_art.stages[lives])