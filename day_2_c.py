# Author: Eric Nguyen


'''
1. Three is a Crowd

•	Make a list of names that includes at least four people.
•	Write an if test that prints a message about the room being crowded, if there are more than three people in your list.
•	Modify your list so that there are only two people in it. Use one of the methods for removing people from the list, don't just redefine the list.
•	Run your if test again. There should be no output this time, because there are less than three people in the list.
•	Bonus: Store your if test in a function called something like crowd_test.
'''


def crowd_test(user_list):
    if len(user_list) > 3:
        print("The room is overcrowded!")


list_names = ["Bob", "Mary", "Ronald McDonald", "Joe"]

crowd_test(list_names)
del list_names[0:2]
print(list_names)
print("Running crowd_test with 2 people in list")
crowd_test(list_names)

'''
2. Three is a Crowd - Part 2
•	Save your program from Three is a Crowd under a new name.
•	Add an else statement to your if tests. If the else statement is run, have it print a message that the room is not very crowded.
'''


def crowd_test_v2(user_list):
    if len(user_list) > 3:
        print("The room is overcrowded!")
    else:
        print("The room is not very crowded.")


'''
Six is a Mob
•	Save your program from Three is a Crowd - Part 2 under a new name.
•	Add some names to your list, so that there are at least six people in the list.
•	Modify your tests so that
•	If there are more than 5 people, a message is printed about there being a mob in the room.
•	If there are 3-5 people, a message is printed about the room being crowded.
•	If there are 1 or 2 people, a message is printed about the room not being crowded.
•	If there are no people in the room, a message is printed abou the room being empty.
'''


def crowd_test_v3(user_list):
    if len(user_list) >= 3 and len(user_list) <= 5:
        print("The room is overcrowded!")
    elif len(user_list) <= 2 and len(user_list) != 0:
        print("The room is not very crowded.")
    elif len(user_list) > 5:
        print("There's a mob in the room!")
    else:
        print("The room is empty.")


list_names2 = ["Bob", "Mary", "Ronald McDonald", "Joe", "Bella", "Amanda"]
print("\nRunning crowd_test_v3")
crowd_test_v3(list_names2)
