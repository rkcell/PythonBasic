mylist=[10,20,30,40,50]

usr_index=input("please enter the index (0-4)")

try:
    result=mylist[int(usr_index)]
    print(result)
except IndexError:
    print("Invalid index, please enter a number between 0 and 4")
except:
    print("Invalid input - please enter a number between 0 and 4")