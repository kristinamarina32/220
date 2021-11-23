"""
Name: Kristina Rydbom
lab12.py

Problem: Lab 12 problems.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from random import randint

# def read_data(filename):
#     my_file = open(filename, "r")
#     i = 0
#     lines = my_file.readlines()
#     my_list = []
#     while i < len(lines):
#         separate = lines[i].split()
#         i = i + 1
#         j = 0
#         while j < len(separate):
#             # convert to numbers
#             val = eval(separate[j])
#             # append
#             my_list.append(val)
#             j = j + 1
#         return my_list
#     # close file
#     my_file.close()
#
#
# def is_in_linear(search_val, values):
#     i = 0
#     while i < len(values):
#         i = i + 1
#         if i == search_val:
#             return True
#     return False


def find_and_remove_first(list, value):
    i = 0
    while i < len(list):
        # i = i + 1
        if list[i] == value:
            list.remove(value)
            list.insert(i, "Kristina")
            # print(list)
            i = len(list)
        i = i + 1


def good_input():
    num = eval(input("Enter a number in the range 1 to 10: "))
    valid_input = 1 <= num <= 10
    while num != valid_input:
        if num < 1:
            print("Input is too low")
            num = eval(input("Enter a number in the range 1 to 10: "))
        if num > 10:
            print("Input is too high")
            num = eval(input("Enter a number in the range 1 to 10: "))
    return num


def num_digits():
    num = eval(input("Enter a positive number: "))
    no_good = num <= 0
    while num != no_good:
        i = 0
        while num > 0:
            i = i + 1
            num = num // 10
        print("Number of digits:", i)
        num = eval(input("Enter a positive number: "))


def hi_lo_game():
    secret_num = randint(1, 100)
    user_guess = eval(input("Enter a number to guess: "))
    i = 6
    print(secret_num)
    while i > 0:
        i = i - 1
        if user_guess < secret_num:
            print("Input is too low")
            user_guess = eval(input("Enter a number to guess: "))
        if user_guess > secret_num:
            print("Input is too high")
            user_guess = eval(input("Enter a number to guess: "))
        if user_guess == secret_num:
            print("Correct")
            print("You win in ", i, " guesses!")
            i = -1
    if i != -1:
        print("Sorry, you lose. The number was ", secret_num, ".")


def main():
    # from algorithms.py
    # read_data("read_data_test_data.txt")
    # values = [1, 2, 3, 4, 5, 22, 7]
    # is_in_linear(5, values)
    # from lab12.py
    # list = [1, 2, 3, 4, 5, 3, 7, 5]
    # find_and_remove_first(list, 5)
    # good_input()
    # num_digits()
    # hi_lo_game()
    pass


main()
