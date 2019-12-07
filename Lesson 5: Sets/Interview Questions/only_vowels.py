'''
Determine whether or not every character in a given string is a vowel.

Ex. "eye" => True
'''

def only_vowels(string):
    vowels = {"a", "e", "i", "o", "u", "y"}
    for i in string:
        if i not in vowels:
            return False
    return True

test = "eye"
print(only_vowels(test))