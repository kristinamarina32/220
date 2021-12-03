"""
Name: Kristina Rydbom
sales_person.py

Problem: HW 10 SalesPerson class.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


class SalesPerson:
    def __init__(self, employee_id, name):
        # initializes employee_id and name to the
        # specified values and sales to an empty list
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        number = 0
        for i in self.sales:
            number += i
        return number

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if self.total_sales() >= quota:
            return True
        return False

    def compare_to(self, other):
        if other.total_sales() > self.total_sales():
            return -1
        elif other.total_sales() < self.total_sales():
            return 1
        return 0

    def __str__(self):
#         want: "Hello my name is <name>"
#         "Hello my name is {0}".format(name)
#         name = Bob
#           gives: Hello my name is Bob.
        return "{0}-{1}: {2}".format(self.employee_id, self.name, self.total_sales())
