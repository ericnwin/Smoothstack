# Author: Eric Nguyen

# 1. Create a function func() which prints a text ‘Hello World’

def print_hello_world():
    print("Hello World")


print_hello_world()

# 2. Create a function which func1(name)  which takes a value name and prints the output “Hi My name is Google’


def print_name(name):
    print(f"Hi my name is {name.capitalize()}")


print_name("eric")

'''
3.Define a function func3(x,y,z) that takes three arguments x,y,z where z is true it will return x and when z is false it should return y . func3(‘hello’goodbye’,false)
'''


def return_x_or_y(x, y, z=True):
    if z == True:
        return x
    else:
        return y


print(return_x_or_y("I'm x", "I'm y", True))
print(return_x_or_y("I'm x", "I'm y", False))

# 4. Define a function func4(x,y) which returns the product of both the values


def product(x, y):
    return x * y


print(product(3, 5))

# 5.Define a function called as is_even that takes one argument , which returns true when even values is passed and false if it is not.


def is_even(value):
    if value % 2 == 0:
        return True
    else:
        return False


print("\nRunning is_even")
print(is_even(3))

'''
6.define a function that takes two arguments ,and returns true if the first value is greater than the second value and returns false if it is less than or equal to the second.
'''


def is_first_arg_greater(x, y):
    if x > y:
        return True
    else:
        return False


print("\nRunning is_first_arg_greater")
print(is_first_arg_greater(2, 3))

'''
7.Define a function which takes arbitrary number of arguments and returns the sum of the arguments.
'''


def sum_args(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


print("\nRunning sum_args")
print(sum_args(5, 2, 3))

'''
8.Define a function which takes arbitrary number of arguments and returns a list containing only the arguments that are even.
'''


def return_even_only(number_list):
    even = []
    for number in number_list:
        if (number % 2) == 0:
            even.append(number)
    return even


print("\nRunning return_even_only")
print(return_even_only([2, 4, 5, 1, 0]))


'''
9.Define a function that takes a string and returns a matching string where every even letter is uppercase and every odd letter is lowercase 
'''


def string_upper_lower(user_string):
    # NOTE: In Python, strings are immutable
    new_string = ""
    for i in range(len(user_string)):
        print(i)
        if i % 2 == 0:
            new_string += user_string[i].upper()

        else:
            new_string += user_string[i].lower()
    return new_string


print(string_upper_lower("smoothstack"))


'''
10.Write a function which gives lesser than a given number if both the numbers are even, but returns greater if one or both or odd.
'''


def greater_or_lesser(x, y):
    if x % 2 == 0 and y % 2 == 0:
        # Print lesser number of x or y
        if x > y:
            print(f"{y} is smaller")
        else:
            print(f"{x} is smaller")
    else:
        # Print greater number of x or y
        if x > y:
            print(f"{x} is greater")
        else:
            print(f"{y} is greater")


greater_or_lesser(2, 4)
greater_or_lesser(3, 6)

'''
11. Write a function which takes  two-strings and returns true if both the strings start with the same letter.
'''


def is_first_letter_the_same(string1, string2):
    if string1[0].lower() == string2[0].lower():
        return True


print(is_first_letter_the_same("apple", "Abs"))

'''
12.Given a value,return a value which is twice as far as other side of it
'''


def squared_value(x):
    return x**2


print("Running squared_value(4)")
print(squared_value(4))

'''
13.A function that capitalizes first and fourth character of a word in a string.
'''


def cap_1st_and_4th(user_string):
    new_string = ''
    if len(user_string) >= 3:
        for i in range(len(user_string)):
            if i == 0 or i == 3:
                new_string += user_string[i].upper()
            else:
                new_string += user_string[i]
    else:
        print("Your string must have at least 4 characters!")
    return new_string


print(cap_1st_and_4th("california"))
