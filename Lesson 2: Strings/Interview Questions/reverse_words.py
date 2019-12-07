'''
Reverse the words in a given string.

Ex. "hi how are you" => "you are how hi"
'''

def reverse_words(string):
    return " ".join(string.split(" ")[::-1])

test = "hi how are you"
print(reverse_words(test))