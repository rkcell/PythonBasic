import random

#list

mylist = [1,1,3,4,5,6]

print(id(mylist[0]))
print(id(mylist[1]))
print(id(1))

color = ["yellow", "white", "black"]
print(id(color[0]))
color[0]="blue"
print(id(color[0]))

print(len(color))

color.append("red")
print(len(color))
print(color)

computer_choice = random.choice(color)
print(computer_choice)
print(id(computer_choice))

computer_choice= random.randint(1,100)
print(computer_choice)
print(id(computer_choice))

# number = 98
#
# ateuli = 98//10
# erteuli = 98%10






# mystring1 ="Hello"
# mystring2 = "Smart Academy"
#
# print(mystring1+mystring2)
# print(mystring1*3)
# print(mystring1[4::-1])




# number1 = 80
# number2 =50
# user_input = int(input("Enter number: "))
#
# if user_input >1 and user_input <=100:
#     if user_input <=80 and user_input >=50:
#         print("You win!")
#     elif user_input >80 or user_input <50:
#         print("Sorry, try later!")
# else:
#     print("Outside the range 1-100!")








# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))
#
# if number1 > number2:
#     print(f"Number 1 {number1} is bigger")
# elif number1 < number2:
#     print(f"Number 2 {number2} is bigger!")
# else:
#     print(f"Numbers are equal!")