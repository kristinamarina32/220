"""
Name: Kristina Rydbom
sales_force.py

Problem: HW 10 SalesForce class.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


class SalesForce:

    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        # reads in file and separates each line by spaces, adds each line to people list
        file = open(file_name, "r")
        for line in file.readlines():
            them = line.split(", ")

            self.sales_people.append(them)
        file.close()
            # ????

    def quota_report(self, quota):


    def top_seller(self):

    def individual_sales(self, employee_id):


