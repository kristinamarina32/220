"""
Name: Kristina Rydbom
weighted_average.py

Problem: Develop a Python program that uses numeric data from a text file.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def weighted_average(in_file_name, out_file_name):
    # open the files
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")

    weighted_average_list = []
    for line in infile:
        each = line.split()
    grades = []
    weights = []
    weighted_avg = 0
    for i in range(2, len(each), 2):
        num_weight = eval(each[i])
        weights.append(num_weight)
    for i in range(3, len(each), 2):
        num_grade = eval(each[i])
        grades.append(num_grade)
    for i in range(len(grades)):
        weighted_avg = ((weights[i]) * (grades[i])) + weighted_avg
        final_weight_average = weighted_avg / 100
        weighted_average_list.append(final_weight_average)
        # print(allValues[0] + "" + allValues[1] + "s average: {0:.1f}".format(finalWeightAverage))
        total_average_weighted = (sum(weighted_average_list) / len(weighted_average_list))
        outfile.write(each[0] + "" + each[1] + "s average: {0:.1f}".format(final_weight_average))
        print("\nClass Average: ", total_average_weighted)
    if total_average_weighted < 100:
        print("Error: the weight is too low")
    if total_average_weighted > 100:
        print("the weight is too high")
#
    infile.close()
    outfile.close()
#
#
# def weighted_average(in_file_name, out_file_name):
#     # open the files
#     infile = open(in_file_name, "r")
#     outfile = open(out_file_name, "w")
#     # empty list
#     weighted_averages_list = []
#     var = infile.readlines()
#
#     for line in var:
#         each = line.split(":")
#         name = each[0]
#         nums = each[1]
#
#         print(name + "\n" + nums + "", file=outfile)
#
#     # if var < 100:
#     # print("the weight is too high/too low")
#
#         grades = []
#         weights = []
#         weighted_average2 = 0
#     #
#         for i in range(2, len(each), 2):
#             num_weight = eval(each[i])
#             weights.append(num_weight)
#         #
#         for i in range(3, len(each), 2):
#             num_grade = eval(each[i])
#             grades.append(num_grade)
#         #
#         for i in range(len(grades)):
#             weighted_average2 = ((weights[i]) * (grades[i])) + weighted_average2
#             final_weight_average = weighted_average2 / 100
#             weighted_averages_list.append(final_weight_average)
#             print(each[0] + " " + each[1] + "s average: {0:.1f}".format(final_weight_average))
#     total_average_weighted = (sum(weighted_averages_list) / len(weighted_averages_list))
#     print("Class Average: ", total_average_weighted)
#     if total_average_weighted < 100:
#         print("Error: the weight is too low")
#     if total_average_weighted > 100:
#         print("the weight is too high")
#
#     infile.close()
#     outfile.close()
#

def main():
    weighted_average("grades.txt", "avg.txt")

    pass


main()
