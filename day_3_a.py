# Author: Eric Nguyen
import random
'''
1.	 Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included). Go to the editor
'''

range_of_num = range(1500, 2701, 1)
num_div7_div5 = []
for num in range_of_num:
    if num % 7 == 0 and num % 5 != 0:
        num_div7_div5.append(num)
print(num_div7_div5)

'''
2.	 Write a Python program to convert temperatures to and from celsius, fahrenheit. Go to the editor
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ] 
Expected Output : 
60°C is 140 in Fahrenheit
45°F is 7 in Celsius 
'''


def temp_conversion(temp, celsius_or_fahrenheit):
    if celsius_or_fahrenheit.lower() == 'f':
        converted_temp = (temp - 32) * 5 / 9
        print(f"{temp}°F is {int(converted_temp)} in Celsius")
    elif celsius_or_fahrenheit.lower() == 'c':
        converted_temp = (temp * 9/5) + 32
        print(f"{temp}°C is {int(converted_temp)} in Fahrenheit")


print("\n")
temp_conversion(60, "C")
temp_conversion(45, 'f')

'''
3.	 Write a Python program to guess a number between 1 to 9. Go to the editor
Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.
'''
print('\n')


def guess_number(n):
    """Will randomly pick a number from 1 to n. User will be prompted to enter a number and correctly guess the random number.

    Args:
        n ([integer]): number
    """
    random_number = random.randrange(1, n)
    user_input = 0
    print(f"A random number from 1 to {n} has been chosen!")
    while (user_input != random_number):
        user_input = int(input("Guess the number: "))
    print("Well guessed!")


# guess_number(9)

'''
4. Write a Python program to construct the following pattern, using a nested for loop.
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
'''


def generate_triangle(pattern="*"):

    for i in range(10):
        #print(f"i: {i}")
        if i > 5:
            i = i -
        print(pattern * i)


generate_triangle()
