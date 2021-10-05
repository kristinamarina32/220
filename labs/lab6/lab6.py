"""
Name: Kristina Rydbom
lab6.py

Problem: Complete lab 6 problems.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def name_reverse():
    string = str(input("Enter a person's name in first-last order: "))
    name = string.split()
    print(name[1], ",", name[0])


def company_name():
    domain = str(input("Enter a three-part internet domain: "))
    company = domain.split(".")
    print(company[1])


def initials():
    # ask user for number of students
    num_of_names = eval(input("How many names will be input?"))
    for num in range(num_of_names):
        string_one = str(num + 1)
        first = input("Enter the first name of student " + string_one + ": ")
        last = input("Enter " + first + "'s last name: ")
        first_initial = first[0]
        last_initial = last[0]
        name = first_initial + last_initial
        print(first + "'s initials are: ", name)


def names():
    # Ask the user to enter a list of names, first and last only, separated by commas
    # For each name, the function should output the initials.
    list_of_names = str(input("Enter a list of names, first and last only, separated by commas: "))
    individual = list_of_names.split(",")
    print("The initials are: ")
    for i in range(len(individual)):
        each = individual[i].split()
        first = each[0]
        last = each[1]
        first_initial = first[0]
        last_initial = last[0]
        name = first_initial + last_initial
        print(name, end=" ")
    # kristina rydbom, khristine mercader, tea lungarini, dajanae sanders


def thirds():
    # Ask how many sentences will be input.
    # The function then asks the user for that many sentences
    # once finished, outputs every third character of each sentence, beginning with the third character.
    num_of_sentences = eval(input("How many sentences will be input?"))
    for num in range(num_of_sentences):
        string_one = str(num + 1)
        sentence_num = input("Enter sentence " + string_one + ":")
        for i in range(2, len(sentence_num), 3):
            print(sentence_num[i], end=" ")
    # The quick brown fox jumps over the lazy dog
    # needs some fixing


def word_average():
    num_of_sentences = eval(input("How many sentences will be input?"))
    for num in range(num_of_sentences):
        string_one = str(num + 1)
        sentence = input("Enter sentence " + string_one + ":")
        words = sentence.split()
        total_average = len(words)
        print(total_average)



# It should calculate the average word length in a sentence entered by the user.
# use a loop


# def pig_latin():
# hm


def main():
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    word_average()
    # pig_latin()
    # add other function calls here


main()
