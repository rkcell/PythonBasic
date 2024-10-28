#Task1 Calculate % of Uppercase and Lowercase characters in the user input string

user_input=input("Please enter the string to calculate % of uppercase and lowercase characters: ")

strlen=0
count_uppercase=0
count_lowercase=0

for c in user_input: #cikli Titoeuli didi asos dasaTvlelad
    if c.isalpha(): #gamovricxod ara-alphabetic simboloebi
        strlen+=1
        if c.isupper():
            count_uppercase+=1
        else:
            count_lowercase+=1


result_upper=round(count_uppercase/strlen*100,2)
result_lower=round(count_lowercase/strlen*100,2)

print(f"Upper Case %: {result_upper}")
print(f"Lower Case %: {result_lower}")

