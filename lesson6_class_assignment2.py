# Task 2: Reverse a String
# Problem: Write a Python program that takes a string input from the user and prints the string in
# reverse using a for loop.
# Example:
# User inputs: 'hello'
# Output: 'olleh'

string = input("Please enter string: ")

string_reversed = string[::-1]


print(string_reversed)

#Part 2
string_reversed =''

for i in range(len(string) - 1, -1, -1):
    string_reversed  += string[i]

print(string_reversed)