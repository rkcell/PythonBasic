# Task 4: Replace Vowels in a String
# Problem: Write a Python program that takes a string and replaces all the vowels (a, e, i, o, u) with
# the * symbol using a for loop.
# Example:
#
# # User inputs: 'apple'
# # Output: '*ppl*'

mystring = input("Please enter a string: ")
vowels = ["a", "e", "i", "o", "u"]
newstring =""
for i in mystring:
    if i in vowels:
        i="*"
    newstring+=i

print(newstring)
