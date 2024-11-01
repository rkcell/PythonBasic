usr_num=input("enter number to convert to integer: ")

try:
    result=int(usr_num)
    print(f"result is: {result}")
except:
    print("Invalid input, please enter a number")