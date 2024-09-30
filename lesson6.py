import random

words = ["pizza",'apple',"plane","teeth","shirt"]
lives = 9
secret_word=random.choice(words)

clue = list("?????")
print(clue)

heart_symbol = u'\u2764'

while lives >0:
    print("Lives left:" + heart_symbol*lives)
    guess = input("Guess letter or word: ")
    lives +=1
