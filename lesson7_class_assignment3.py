# Check if a String is a Palindrome
# Write a function `is_palindrome` that checks if a given string is a palindrome (a word that reads the
# same forward and backward).

def is_palindrome(user_input):
    clean_string = user_input.replace(" ", "").lower()

    if clean_string == clean_string[::-1]:
        return True
    else:
        return False



print(is_palindrome("madam")) # Output: True
print(is_palindrome("hello")) # Output: False