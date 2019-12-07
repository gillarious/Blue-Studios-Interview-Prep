'''
Create a method that determines whether or not a given string is a palindrome.

Ex. "radar" => True
'''

def is_palindrome(word):
    return word == word[::-1]

test = "radar"
print(is_palindrome(test))