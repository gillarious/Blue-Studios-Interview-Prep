'''
In a given string, remove all the characters from the string which have already appeared in it.

Ex. "ccbaacc" => "cba"
'''

def remove_duplicates(string):
    s = set()
    for i in string:
        s.add(i)
    return "".join(s)

test = "ccbaacc"
print(remove_duplicates(test))