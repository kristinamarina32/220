"""
Name: Kristina Rydbom
lab8.py

Problem: Complete lab 8 problems.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def number_words(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")
    # process each line of the input file
    total = 0
    for line in infile:
        each = line.split()
        for i in each:
            total += 1
            outfile.write(str(total) + " " + i + "\n")

    infile.close()
    outfile.close()


def hourly_wages(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")
    for line in infile:
        each = line.split()
        wage = each[2]
        new_wage = float(wage) + 1.65
        hours_worked = each[3]
        earned = new_wage * float(hours_worked)
        print(earned)
        first = each[0]
        last = each[1]
        outfile.write(first + " " + last + " " + str(earned) + "\n")

    infile.close()
    outfile.close()


def calc_check_sum(isbn):
    # that accepts as a parameter a string representing an ISBN and returns the checksum as an int.
    total = 0
    for i in range(10, 0, -1):
        multiply = int(isbn[10-i]) * i
        total = total + multiply

    return total


def send_message(file, friend):
    my_file = open(file, "r")
    friend_file = open(friend, "w")
    for line in my_file:
        each = line.split()
        for word in each:
            friend_file.write(str(word) + " ")

    my_file.close()
    friend_file.close()


def send_safe_message(file, friend, key):
    my_file = open(file, "r")
    friend_file = open(friend, "w")
    for line in my_file:
        each = line.split()
        for word in each:
            friend_file.write(str(word) + " ")

    message = str(word) + " "
    key = eval(input("Enter an integer key value: "))
    for i in range(len(message)):
        ordinal = ord(message[i])
        combo = ordinal + key
        character = chr(combo)
        print(character, end="")

    my_file.close()
    friend_file.close()


def main():
    # number_words("walrus.txt", "new.txt")
    # hourly_wages("hourly_wages.txt", "new_hourly_wages.txt")
    # calc_check_sum("0072946520")
    # send_message("message.txt", "bob.txt")
    send_safe_message("secret_message.txt", "bob.txt", "3")



    # add other function calls here
    pass


main()
