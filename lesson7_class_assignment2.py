# Write a function `count_vowels` that takes a string and returns the number of vowels (`a, e, i, o, u`)
# in the string.


def count_vowels(thestring):
    vowels = 'a, e, i, o, u'
    counter=0
    for i in thestring:
        if i in vowels:
            counter+=1

    return counter


print(count_vowels("hello"))