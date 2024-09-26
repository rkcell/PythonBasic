# number=9
# if number in range(10):
#     print("yes")
# else:
#     print("No")

number1 = int(input("Enter first number: "))
operation = input("Enter arithmetic operation symbol (/ * + -): ")
number2 = int(input("Enter second number: "))

if operation == "/":
    print(int(number1/number2))
elif operation == "*":
    print(int(number1 * number2))
elif operation == "+":
    print(int(number1 + number2))
elif operation == "-":
    print(int(number1 - number2))
else:
    print("Please input valid data")