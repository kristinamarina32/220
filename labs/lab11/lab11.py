"""
Name: Kristina Rydbom
lab11.py

Problem: Lab 11 problems.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import random


def word_list(in_file_name):
    infile = open(in_file_name, "r")
    # read each line of the input file and place into a list
    lines = infile.readlines()
    # close file
    infile.close()
    # return
    return lines


def random_word(lines):
    # choose random line and return in all lowercase
    random_before = random.choice(lines)
    random_choice = random_before.lower()
    return random_choice


def chosen_word(random_choice, guess, past_guesses):
    # create an empty list, and then add the characters in random_choice to the "word" list
    word = []
    for ch in random_choice:
        word.append(ch)
    # asking user for letter input and making sure their input is lowercase
    # letter = input("Enter a letter to guess: ")
    # guess = letter.lower()
    # creating an empty string, if the guess == any of the characters in the word, the string will now have the guess
    # if the places in the string do not have any characters from the word, it will just have "_" for that place
    guessed_word = ""
    for i in range(len(word)-1):
        if guess == word[i]:
            guessed_word += guess
        elif word[i] in past_guesses:
            guessed_word += word[i]
            return guessed_word
        else:
            guessed_word += "_"
    return guessed_word


def all_letters_guessed(guessed_word):
    # to see if all of the letters have been guessed
    # if user has guessed all of the letters, return True
    # if not, return False
    if "_" not in guessed_word:
        return True
    if "_" in guessed_word:
        return False


def actual_game():
    lines = word_list("wordlist.txt")
    random_choice = random_word(lines)
    # mistakes = 7
    guessed_word = chosen_word(random_choice)
    while not all_letters_guessed(guessed_word):
        print(chosen_word(random_choice))
    if all_letters_guessed(guessed_word):
        print("GAME COMPLETE")


def main():
    # add other function calls here
    lines = word_list("wordlist.txt")
    random_choice = random_word(lines)
    guessed_word = chosen_word(random_choice)
    all_letters_guessed(guessed_word)
    actual_game()

    pass


main()
