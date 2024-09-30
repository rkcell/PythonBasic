numbers = [1, 2, 3, 1, 4, 1, 5]

counter=0
user_input=int(input("Enter number: "))
for i in numbers:
    if i == user_input:
        counter+=1

print(f"{user_input} appears {counter} times")

