# ლოტოს გათამაშება
# თქვენი მიზანია შექმნათ ლოტოს გათამაშების პროექტი.
# მოცემულია:
# numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]
# მომხმარებელმა უნდა აირჩიოს 6 სხვადასხვა რიცხვი 1:42 შუალედიდან, რომლისგანაც შეიქმნება ლოტოს ბილეთი (გამოიყენეთ while loop).
# გათამაშებიდან რეალურად ამოსული 6 სხვადასხვა რიცხვი უნდა იყოს შემთხვევითი. უნდა შეადაროთ თქვენი ბილეთი გათამაშებიდან ამოსულ რიცხვებს და:
# 1. თუ ბილეთის 1 ან 0 რიცხვი დაემთხვა რეალურად ამოსულ რიცხვს, უნდა დაიპრინტოს 'თქვენმა ბილეთმა ვერ მოიგო'.
# 2. თუ 1-ზე მეტი და 4-ზე ნაკლები რიცხვი დაემთხვევა რეალურად ამოსულ რიცხვს, უნდა დაიპრინტოს 'თქვენ მოიგეთ 100-1000 ლარის ფარგლებში'.
# 3. თუ 4 ან მასზე მეტი და 6-ზე ნაკლები რიცხვი დაემთხვევა რეალურად ამოსულ რიცხვს, უნდა დაიპრინტოს 'თქვენ მოიგეთ 1000-5000 ლარის ფარგლებში'.
# 4. სხვა შემთხვევაში უნდა დაიპრინტოს 'თქვენ მოიგეთ ჯეკპოტი!'
# ამასთან ერთად გაითვალისწინეთ, როდესაც ვირჩევთ 6 რიცხვს შემთხვევით, ეს რიცხვები გადაიტანეთ list-ში თუმცა  ერთი და იგივე რიცხვი არ უნდა ამოვიდეს ბევრჯერ,
# ვიცი რთულია ამ პრობლემის გადაჭრა, თუმცა ეცადეთ რამე მოიფიქროთ
# მაგალითად:
# random_numbers  = [1,1,2,5,29,5] ასე თუ დაჯდა რიცხვები, მაშინ პრობლემა გვექნება, სიაში ყველა რიცხვი უნდა იყოს უნიკალური.

import random

numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]
user_numbers=[]
random_numbers=[]
i=1

print("Input 6 numbers of your '6 of 42' lottery ticket!")
#create the list of unique user numbers list:
while len(user_numbers)<6:
    user_input=int(input(f"Enter number N{i}: "))
    if user_input in numbers:
        if user_input in user_numbers:
            print("This number is already exist in your lottery ticket! Enter different number")
            continue
        else:
            user_numbers.append(user_input)
            i+=1
    else:
        print("Please enter integer from 1 to 42: ")

#create the list of unique random numbers list:
while len(random_numbers)<6:
    computer_choice = random.choice(numbers)
    if computer_choice in random_numbers:
        continue
    else:
        random_numbers.append(computer_choice)

print("Your ticket is: ", user_numbers)
print("Lottery draw is: ",random_numbers)

#check the resulting coincidence
howmany=0
for j in range(6):
    if user_numbers[j] in random_numbers:
        howmany+=1
print("Coincidence of", howmany, "from 6")

#output the results
if howmany <=1:
    print("You didn't win!")
elif howmany <4:
    print("You win between 100 and 1000 GEL!")
elif howmany <6:
    print("You win between 1000 and 5000 GEL!")
else:
    print("YOU WIN THE JACKPOT!")