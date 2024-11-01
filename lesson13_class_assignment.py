

x = int(input("enter x: "))
y = int(input("enter y: "))

try:
    result = x/y
    print(result)
except ZeroDivisionError:
    print("division by zero!")