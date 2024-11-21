'''
დაწერეთ პროგრამა, რომელიც ფუნქციაში მიიღებს მომხმარებლის დაბადების წელს, გამოითვლის მიმდინარე წლის მიხედვით
მის ასაკს და გამოთვლილი ასაკის მიხედვით შექმნის საქაღალდე "Ages",
რომელშიც შეიქმნება იმდენივე დანომრილი ტექსტური ფაილი, რამდენი წლისაცაა მომხმარებელი.

მაგ. მომხმარებელმა შეიტანა დაბადების წელი 2010. პროგრამაში ფუნქციამ უნდა გამოთვალოს რომ ის 13 წლისაა.
შემდეგ პროგრამულად იქმნება "Ages" საქაღალდე და მასში მოთავსებულია 13 ცალი ტექსტური ფაილი:
1.txt
2.txt
3.txt
...
თვითონ ფაილებშიც (შიგნით) უნდა იყოს გაწერილი შესაბამისი წელი, მაგ.:
1.txt ფაილის შიგთავსი -> 1
2.txt ფაილის შიგთავსი -> 2
და ა.შ.
'''
from datetime import datetime
import os

def calculate_age(birth_year):
    current_year = datetime.now().year
    age = current_year - birth_year
    return age

def create_files(age):
    folder_name = "Ages"
    if os.path.isdir(folder_name):
        print(f"Directory {folder_name} exists. Entering it...")
    else:
        print(f"Directory {folder_name} does not exist. Creating...")
        os.mkdir(folder_name)
    os.chdir(folder_name)
    for i in range(1,age+1):
        f = open(f"{i}.txt", "w")
        f.write(f"{i}")
        print(f"File {i}.txt written")
        f.close()

def main():
    year_of_birth = int(input("Enter your year of birth: "))
    age=calculate_age(year_of_birth)
    print(f"Your age is: {age} years")
    try:
        create_files(age)
    except:
        print("Error occurred writing files")

if __name__ == '__main__':
    main()