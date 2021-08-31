"""
Name: <Kristina Rydbom>
lab1.py

Problem: This function calculates the area of a rectangle
"""


def calc_rec_area():
    length = eval(input("Enter the length:"))
    width = eval(input("Enter the width:"))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length:"))
    width = eval(input("Enter the width:"))
    height = eval(input("Enter the height:"))
    volume = length * width * height
    print("Volume =", volume)


def shooting_percentage():
    total_shots = eval(input("Enter total shots:"))
    shots_made = eval(input("Enter shots made:"))
    total_shooting_percentage = shots_made / total_shots
    print("Total shooting percentage=", total_shooting_percentage)


def coffee():
    pounds_of_coffee_purchased = eval(input("Enter pounds of coffee purchased:"))
    total_cost = (0.86 * pounds_of_coffee_purchased) + (10.56 * pounds_of_coffee_purchased) + 1.50
    print("Total cost=", total_cost)


def kilometers_to_miles():
    kilometers_traveled = eval(input("Enter kilometers traveled:"))
    number_of_miles_traveled = (kilometers_traveled * 1) / 1.61
    print("Number of miles traveled=", number_of_miles_traveled)




