import random
from words import Words
import string

def get_valid_word(Words):
    """gets a valid word from the list of words in words.py"""
    word = random.choice(Words)
    while '-' in word or ' ' in word:
        word = random.choice(Words)
    
    return word.upper()

def hangman():
    word = get_valid_word(Words)
    word_letters = set(word)
    alphabets = set(string.ascii_uppercase)
    used_letters = set()
    
    lives = 6
    while len(word_letters) > 0 and lives > 0:
        
        print("You have", lives, "lives and have used the following letters", ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word is", ' '.join(word_list))
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabets - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                if lives == 1:
                    lives -= 1
                    print("Letter not in word")
                else:
                    lives -= 1
                    print("Letter not in word; please guess again")
        elif user_letter in used_letters:
            print("You have already used this letter; please guess another letter")

        else:
            print("Invalid guess; please guess a valid letter")

    if lives == 0:
        print("Sorry, you are dead :(; the word was", word)
    else:
        print("Yay! You have guessed the word", word, "correctly!!")

hangman()