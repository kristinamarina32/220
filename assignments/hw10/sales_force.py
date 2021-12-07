"""
Name: Kristina Rydbom
sales_force.py

Problem: HW 10 SalesForce class.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from sales_person import SalesPerson


class SalesForce:

    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        # reads in file and separates each line by spaces, adds each line to people list
        file = open(file_name, "r")
        for line in file.readlines():
            them = line.split(", ")
            parm = SalesPerson(int(them[0]), them[1])
            individual_sales = them[2].split(" ")
            for each in individual_sales:
                float_sales = float(each)
                parm.enter_sale(float_sales)
            self.sales_people.append(parm)
        file.close()

    def quota_report(self, quota):
        # returns a list where each element is itself a list of each seller's employee_id, name, total sales, and a
        # boolean value of whether or not they hit the specified quota- true if they hit it, false if they did not
        big_list = []
        for group in self.sales_people:
            little_list = [group.get_id(), group.get_name(), group.total_sales(), group.met_quota(quota)]
            big_list.append(little_list)
        return big_list

    def top_seller(self):
        highest_sales = [self.sales_people[0]]
        for sale in self.sales_people:
            if highest_sales[0].compare_to(sale) == -1 or highest_sales[0].compare_to(sale) == 0:
                highest_sales = [sale]
            elif highest_sales[0].compare_to(sale) == 0:
                highest_sales.append(sale)
        return highest_sales

    # loop through and compare each current max to each one and yeah set max to be new max item in list
    def individual_sales(self, employee_id):
        for each in self.sales_people:
            i_d = each.get_id()
            if i_d == employee_id:
                return each
        return None
