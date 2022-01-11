# Author: Eric Nguyen

# Coding Exercise 4:
# 1.	Create a list with one number, one word and one float value. Display the output of the list.
list = [6, "word", 4.2]
print(list)

# 2.	I have a nested list [1,1,[1,2]], how to grab the value of 2 from the list.

list = [1, 1, [1, 2]]
# accessing 3rd element with [2] and within 3rd element we're accessing the 2nd element with [1]
print(list[2][1])

# 3.	lst=['a','b','c'] What is the result of lst[1:]?
lst = ['a', 'b', 'c']
print(lst[1:])  # Output should be from 2nd element to end of list [b ,c]

# 4.	Create a dictionary with weekdays as keys and week index numbers as values.do assign dictionary to a variable
week = {"Monday": 0, "Tuesday": 1, "Wednesday": 2,
        "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}
for weekday, index_num in week.items():
    print(f"{weekday} corresponds to index {index_num}")

# 5.	D={‘k1’:[1,2,3]} what is the output of d[k1][1]
D = {'k1': [1, 2, 3]}
# will go inside key "k1" and output 2nd element [2] in the list
print(D['k1'][1])

# 6.	Can you create a list [1,[2,3]] into a tuple
my_list = [1, [2, 3]]
my_tuple = (my_list)
print(my_tuple)
print(type(my_tuple))

# 7.	With a single set function can you turn the word ‘Mississippi’ to distinct character word
word = "Mississippi"
unique = set(word)
print(unique)

# 8.	Can you add an element ‘X’ to the above created set
unique.add("X")
print(unique)

# 9.	Output of set([1,1,2,3])
print(set([1, 1, 2, 3]))  # output is {1,2,3}

'''
  10. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,between 2000 and 3200 (both included).
	The numbers obtained should be printed in a comma-separated sequence on a single line.
	Hints: 
	Consider use range(#begin, #end) method
'''
range_of_num = range(2000, 3201, 1)
num_div7_div5 = []
for num in range_of_num:
    if num % 7 == 0 and num % 5 != 0:
        num_div7_div5.append(num)
print(num_div7_div5)

'''
	11. Write a program which can compute the factorial of a given numbers.
	The results should be printed in a comma-separated sequence on a single line.
	Suppose the following input is supplied to the program:
	8
	Then, the output should be:
	40320

'''


def factorial(number):
    count = 1
    if number == 0:
        return 1
    else:
        while(number > 0):
            count *= number
            number -= 1
        return count


x = int(input("\nEnter number to calculate factorial: "))
print(factorial(x))


'''
    12. With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
	Suppose the following input is supplied to the program:
	8
	Then, the output should be:
	{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
'''


def generate_dictionary_squared(n):
    squared_dictionary = {}
    for i in range(1, n + 1):
        squared_dictionary[i] = i*i
    print(squared_dictionary)


print("\n")
generate_dictionary_squared(5)

'''
    13. Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
	Suppose the following input is supplied to the program:
	34,67,55,33,12,98
	Then, the output should be:
	['34', '67', '55', '33', '12', '98']
	('34', '67', '55', '33', '12', '98')
'''


def generate_tuple(user_list):
    print(f"\n{user_list}")
    return tuple(user_list)


print(generate_tuple(['34', '67', '55', '33', '12', '98']))

'''
    14. Define a class which has at least two methods:
	getString: to get a string from console input
	printString: to print the string in upper case.
	Also please include simple test function to test the class methods.
'''


class String_example:
    def __init__(self):
        self.user_string = ""

    def getString(self):
        user_string = input("Enter a string: ")
        self.user_string = user_string

    def printString(self):
        print(self.user_string.upper())


string1 = String_example()

string1.getString()
string1.printString()
