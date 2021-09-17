"""
Name: Kristina Rydbom
interest.py

Problem: Write a program that computes the monthly interest charge on a credit card account.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():
    #input
    annual_interest_rate = eval(input("Enter the annual interest rate: "))
    billing_cycle = eval(input("Enter the number of days in the billing cycle: "))
    previous_net_balance = eval(input("Enter previous net balance: "))
    payment_amount = eval(input("Enter payment amount: "))
    day_of_payment = eval(input("Enter the day of the billing cycle the payment was made: "))

    #calculations
    step_1 = (previous_net_balance * billing_cycle)
    step_2 = (payment_amount * (billing_cycle - day_of_payment))
    step_3 = step_1 - step_2
    step_4 = step_3 / billing_cycle
    average_daily_balance = step_4
    monthly_interest_charge = average_daily_balance * (annual_interest_rate / 12 / 100)
    print(round(monthly_interest_charge, 2))


if __name__ == '__main__':

    main()
