# Author: Eric Nguyen

'''
1.	Imagine an accounting routine used in a book shop. It works on a list with sublists, which look like this: 
Order Number	Book Title and Author	Quantity	Price per Item
34587	Learning Python, Mark Lutz	4	40.95
98762	Programming Python, Mark Lutz	5	56.80
77226	Head First Python, Paul Barry	3	32.95
88112	Einführung in Python3, Bernd Klein	3	24.99

Write a Python program, which returns a list with 2-tuples. Each tuple consists of a the order number and the product of the price per items and the quantity. The product should be increased by 10€ if the value of the order is smaller than 100 €. 
Write a Python program using lambda and map.

'''
book_orders = [["34587", "Learning Python, Mark Lutz", 4, 40.95],
               ["98762", "Programming Python, Mark Lutz", 5, 56.80],
               ["77226", "Head First Python, Paul Barry", 3, 32.95],
               ["88112", "Einfuhrung in Python3, Bernd Klein", 3, 24.99]]

# Minimum threshold for the orders, else add $10
min_order = 100

# Creating a list of (order_number, price * quantity)
extracted_data_of_order_price_quantity = map(lambda x: (x[0], x[2] * x[3]), book_orders)

# Editing list to account for orders below min_order
totals = list(map(lambda x: (x[0], x[1] + 10) if (x[1] < min_order) else x , extracted_data_of_order_price_quantity))
print(totals)

for order in totals:
 print(f"Order# {order[0]} has a total invoice amount of ${order[1]:.2f}")