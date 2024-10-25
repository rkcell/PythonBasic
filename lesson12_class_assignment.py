# given_string='car, bus, plane, box, car, tree, sky, plane'
#
# # mylist=given_string.split(',')
# # for x in range(len(mylist)):
# #     mylist[x]=mylist[x].strip()
#
# find_str=input("Please enter which word you need to replace: ").strip()
# replace_str=input("Input to replace with word: ").strip()
#
# given_string=given_string.replace(find_str,replace_str)
#
#
# print(given_string)

def check_chr(word):
    print(f"Length of the word {word} is {len(word)}")
    return len(word)

def average(a,b,c):
    print(f"Average of {a}, {b}, {c} is:   {(a+b+c)/3}")
    return (a+b+c)/3

def main():
    while True:
        select = int(input("Please enter the number you need to run: "))
        if select==1:
            input_word=input("Please enter word to coun characters:")
            check_chr(input_word)
            break
        elif select ==2:
            a=int(input("For average of ABC, enter A: "))
            b=int(input("For average of ABC, enter B: "))
            c=int(input("For average of ABC, enter C: "))
            average(a,b,c)
            break
        else:
            print("Please input 1 or 2")

main()