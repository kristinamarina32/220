"""
Name: Kristina Rydbom
traffic.py

Problem: Write a program that will help analyze traffic patterns.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():
    # ask user for roads surveyed
    roads_surveyed = eval(input("How many roads were surveyed?"))
    num_of_vehicles = 0
    avg = 0
    avg_num_of_vehicles = 0

    # for loop
    for num in range(roads_surveyed):
        string_one = str(num + 1)
        days_surveyed = eval(input("How many days was road " + string_one + " surveyed?"))
        end = 0

        for i in range(days_surveyed):
            string_two = str(i + 1)
            cars = eval(input("How many cars traveled on day " + string_two + "?"))
            end += cars
            avg = end / days_surveyed
            # calculate total number of vehicles traveled on all roads
            num_of_vehicles += cars
            # calculate average number of vehicles per road
            avg_num_of_vehicles = num_of_vehicles / roads_surveyed

    # print
        print("Road average vehicles per day: ", round(avg, 2))
    print("Total number of vehicles traveled on all roads: ", round(num_of_vehicles, 2))
    print("Average number of vehicles per road: ", round(avg_num_of_vehicles, 2))


if __name__ == '__main__':
    main()