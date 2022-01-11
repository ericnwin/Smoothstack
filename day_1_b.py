# Author: Eric Nguyen
from tabulate import tabulate


# Problem 1.	Numbers: Example code to add two numbers 50+50 and 100-10 and print it.
print(50 + 50, 100 - 10)

# Problem 2.	30+6,6^6,6**6,6+6+6+6+6+6
print(30 + 6, 6 ** 6, 6**6, 6+6+6+6+6+6)

# Problem 3.	Print “Hello World” on the console output. Print output “Hello World : 10”
# Make sure capitalization and spacing matches.

print("Hello World", "Hello World : 10\n")

""" Problem 4.	Below is a mathematical calculation exercise  :
Mathematically, mortgage works by the following algorithm:
•	Joel borrows big money sum P from bank (and performs purchase);
•	bank tells him its interest rate R in percents - the speed of growth of the debt;
•	at the end of each month the debt is increased by R / 12 percents;
•	immediately after it Joel gives to bank some predefined small sum M to decrease the debt;
•	debt is considered settled when its value is reduced to zero (this could take several years).
For example, Joel takes P = $800,000 from bank with interest rate of R = 6%. He is willing to pay M = $10000 at the end of each month.
"""

# given inputs Principal (amount of loan), Interest Rate, Length of time to pay out in months
# Return M (required monthly payment rounded up to whole dollars)


def monthly_payment(principal, interest_rate, period):
    interest_rate = interest_rate / (12 * 100)
    x = (1 + interest_rate) ** period
    payment_amount = principal * (interest_rate * x) / (x - 1)
    number = 1
    balance = principal
    headers = ['Month', 'Payment Amount',
               'Interest', 'Principal Paid', 'Balance']

    while number <= period:
        interest = balance * interest_rate
        principal = payment_amount - interest
        balance = balance - principal
        data = [round(number, 1), round(payment_amount, 2),
                round(interest, 2), round(principal, 2), round(balance, 2)]

        print(tabulate([data], headers, tablefmt="pretty"))
        number += 1


"""
class Monthly_Payment():
    def __init__(self, principal, interest_rate, months_to_pay):
        self.principal = principal
        self.interest_rate = interest_rate
        self.months_to_pay = months_to_pay

    def calculate():
        count = 0
        while (count <= 103)
"""
if __name__ == "__main__":
    list_data = [int(item) for item in input(
        "Enter Principal, Interest Rate, and Time in Months\n (Enter data seperated by a space) ").split()]

    example = monthly_payment(int(list_data[0]), int(
        list_data[1]), int(list_data[2]))
