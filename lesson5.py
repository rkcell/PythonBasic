import random

moves = ["rock", "paper", "scissors"]
computer_score=0
user_score=0
counter=0

for i in range(3):
    computer_choice = random.choice(moves)
    user_choice=input("Enter move (rock/paper/scissors: ")
    if computer_choice == user_choice:
        print("Its a tie!")
        user_score+=0.5
        computer_score+=0.5











# numbers = [5,12,43,32,29,54,89]
# max_value=numbers[0]
# for i in range(len(numbers)):
#     if numbers[i]>=numbers[i+1]:
#         max_value=numbers[i]
