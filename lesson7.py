import string

def check_password_strength(password=""):
    #define the criteria
    min_length=8
    special_characters= string.punctuation

    #check conditions

    has_upper=any(i.isupper() for i in password)
    has_lower=any(i.islower() for i in password)
    has_digit=any(i.isdigit() for i in password)
    has_special=any(i in special_characters for i in password)

    if len(password) < min_length:
        return f"Weak password, less than {min_length} is required"

    #criteria check

    elif has_upper and has_lower and has_digit and has_special:
        return True

    else:
        return False


# def get_numbers():
#     numbers=[]
#     for i in range(7):
#         num=int(input("Enter the number: "))
#         numbers.append(num)
#
#     return numbers
#
# print(get_numbers())


# def get_amount(num=0, price=0):
#
#     return num*price
#
# print(get_amount(5,6))


# def get_full_name():
#
#     first_name= input("Enter your first name: ")
#     last_name=input("Enter your last name: ")
#
#     print(f"Your first and last name is: {first_name.capitalize()} {last_name.capitalize()}")
#
# get_full_name()





# #FUNCTIONS:
#
# def print_sum(x,y):
#     print(x+y)
#     return x+y
#
#
# print_sum(3,4)



#
# mystring = " Hello World World Hello World Hello Hello"
# mylist=mystring.split()
# hello_count =0
# print(mylist)
# for i in mylist:
#     if i.lower() == "hello":
#         hello_count +=1
#
# print(f"Hello count is: {hello_count}")


#Palindrome checker: A man a plan a canal Panama
#
# user_input = input("Please enter the string to check for palindrome: ")
# clean_string = user_input.replace(" ", "").lower()
#
# if clean_string==clean_string[::-1]:
#     print("This is palindrome!")
# else:
#     print("Not palindrome!")




#
# mystring = "  Hello World   "
# mystring = mystring.strip()
# mystring = mystring.lower()
# print(mystring)