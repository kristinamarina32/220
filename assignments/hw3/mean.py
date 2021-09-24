import math
"""
Name: Kristina Rydbom
mean.py

Problem: Calculate mean for HW 3.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
# What will the program do? Calculate the mean(s).
# What will be the inputs and outputs? What I presented below.
# What is a step-by-step list of what the program must do, aka an algorithm? Output RMS avg, harmonic mean, and gemetric


def main():

    num_of_values = eval(input("Enter the number of values to be entered: "))
    start = 0
    den = 0
    result = 1

    # loop
    for i in range(num_of_values):
        i = eval(input("Enter value:"))
        start = i**2 + start
        den = (1/i) + den
        result = result * i

    # calculations
    rms_average = math.sqrt(start / num_of_values)
    harmony = (num_of_values / den)
    geometric_mean = result ** (1/ num_of_values)

    # outputs
    print(round(rms_average, 3))
    print(round(harmony, 3))
    print(round(geometric_mean, 3))


if __name__ == '__main__':
    main()