# Task 3: Sum of Even Numbers in a List
# Problem: Write a Python program to calculate the sum of all even numbers in a list. Use a for loop to
# iterate through the list and add the even numbers.
# Example:
# numbers = [1, 2, 3, 4, 5, 6]
# # Output: Sum of even numbers is 12

numbers = [1, 2, 3, 4, 5, 6,8,10,10]
mysum=0

for i in numbers:
    if i%2==0:
        mysum+=i

print(mysum)