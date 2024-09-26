number=0
sum=0
while number >=0:
    number=int(input("Enter number for sum: "))
    if number <0:
        break
    sum+=number

print("Total sum is ", sum)