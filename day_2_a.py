# Author: Eric Nguyen

# 1.	Write a string that returns just the letter ‘r’ from ‘Hello World’
# For example, ‘Hello World’[0] returns ‘H’.You should write one line of code. Don’t assign a variable name to the string.
print("Hello World" [8] + "\n")

# 2.	String slicing to grab the word ‘ink’ from the word  ‘thinker’
# S=’hello’,what is the output of h[1]
print("thinker"[2:5] + "\n")

# 3.	S=’Sammy’ what is the output of s[2:]”
S = "Sammy"
print(S[2:] + "\n")  # Output should be "mmy"

# 4.	With a single set function can you turn the word ‘Mississippi’ to distinct character word.
word = "Mississippi"
print(str(set(word)) + "\n")

# 5. Your goal in this programming exercise is to determine, whether the phrase represents a palindrome or not.
# Input data contains number of phrases in the first line.
# Next lines contain one phrase each.
# Answer should have a single letter (space separated) for each phrase: Y if it is a palindrome and N if not.


def check_if_palindrome():
    number_of_phases = input("Enter number of phrases ")
    count = 1
    list_phrases = []
    answer = []
    while (count <= int(number_of_phases)):
        phrase = input(f"Enter phrase {count}: ")
        list_phrases.append(phrase)
        count += 1

    for phrase in list_phrases:
        # Using .isalnum() to return True if all characters are alphanumeric characters only && using .lower() to remove capitalized characters
        phrase = "".join(
            character for character in phrase if character.isalnum()).lower()

        # phrase[start:stop:step] -> phrase[::-1] is all items in the array, reversed
        if phrase == phrase[::-1]:
            answer.append("Y ")
        else:
            answer.append("N ")
    return answer


if __name__ == "__main__":
    print(check_if_palindrome())
