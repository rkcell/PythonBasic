number = int(input("Enter number: "))
sum=0
fact=1
i=1
for i in range(1,number+1):
    fact*=i
    sum+=fact
print(sum)