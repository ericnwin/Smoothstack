'''
Day 5 –Weekend exercise work – please use functions for this problem
Let us apply our programming skills to some quasi-scientific problem - since it is bit dull to learn only abstract things.
The simple measure of body constitution was proposed at the middle of XIX century. It depends only on the height and weight of a person - and is called Body Mass Index or BMI. It is defined as:
BMI = weight / height^2
Where weight is taken in kilograms and height in meters.
Four general grades are proposed:
Underweight     -           BMI < 18.5
Normal weight   -   18.5 <= BMI < 25.0
Overweight      -   25.0 <= BMI < 30.0
Obesity         -   30.0 <= BMI
For example, if I have weight of 80 kg and height of 1.73 m I can calculate:
BMI = 80 / (1.73)^2 = 26.7
i.e. somewhat overweight.
We will not discuss how proper or improper this gradation is. Instead you should simply calculate grades for several people.
Input data contain number of people in the first line.
Other lines will contain two values each - weight in kilograms and height in metres.
Answer should contain words under, normal, over, obese for each corresponding test-case, separated with spaces. For example:
input data:
3
80 1.73
55 1.58
49 1.91

answer:
over normal under
'''


def calculate_BMI_metric(n):
    """ Uses weight(kg) / height^2 (m) to calculate BMI. Takes in n amount of people and asks for their weight and height

    Args:
        n ([integer]): The amount of people you want to calculate their BMI
    """
    bmi_list = []
    people_data = []
    for i in range(n):
        people_data.append(
            input(f"Enter weight and height for person {i + 1}: "))
    print(people_data)
    #int_people_data = [int(data.split()) for data in people_data]
    for person in people_data:
        print(person)
        print(type(person))
        print(person.split())
        print(list(map(float, person.split())))
        # for weight, height in person.join()
        # returns only 1st digit. Very wonky way to do it
        # print(f"Weight: {person[0]}")


calculate_BMI_metric(2)
