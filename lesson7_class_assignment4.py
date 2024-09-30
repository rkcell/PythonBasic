# Find the Longest Word in a Sentence
# Write a function `longest_word` that takes a sentence (string) and returns the longest word in the
# sentence.

def longest_word(thestring):

    thelist = thestring.split()
    longest=0
    result=""
    for i in thelist:
        if len(i) > longest:
            longest=len(i)
            result=i

    return result

print(longest_word("I love learning Python programming")) # Output: "programming"