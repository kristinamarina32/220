"""
Name: Kristina Rydbom
weighted_average.py

Problem: Develop a Python program that uses numeric data from a text file.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import re

def weighted_average():
    infile_name = str(input("Name of the input file: "))
    outfile_name = str(input("Name of the output file: "))
    # open the files
    infile = open(infile_name, "r")
    outfile = open(outfile_name, "w")
    # empty list
    weighted_averages_list = []

    for line in infile:
        all_values = line.split(" ")

    # for line in outfile:
    #     all_values = line.split()
    grades = []
    weights = []
    weighted_average2 = 0

    for i in range(2, len(all_values), 2):
        num_weight = eval(all_values[i])
        weights.append(num_weight)

    for i in range(3, len(all_values), 2):
        num_grade = eval(all_values[i])
        grades.append(num_grade)

    for i in range(len(grades)):
        weighted_average2 = ((weights[i]) * (grades[i])) + weighted_average2
        final_weight_average = weighted_average2/100
        weighted_averages_list.append(final_weight_average)
        print(all_values[0] + " " + all_values[1] + "s average: {0:.1f}".format(final_weight_average))
        total_average_weighted = (sum(weighted_averages_list)/len(weighted_averages_list))
        print("Class Average: ", total_average_weighted)

    infile.close()
    outfile.close()


# weighted_average()
