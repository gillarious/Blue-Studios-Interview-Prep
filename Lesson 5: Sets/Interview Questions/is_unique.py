'''
Determine whether or not every character in a given string is unique.

Ex. "gate" => True
'''

def is_unique(string):
    s = set()
    for i in string:
        if i in s:
            return False
        s.add(i)
    return True

test = "gate"
print(is_unique(test))