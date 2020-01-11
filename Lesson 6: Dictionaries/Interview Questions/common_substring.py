'''
Check if two strings share a common substring.

Ex. "hello" and "world" => YES
Ex. "pants" and "color" => NO
'''

def common_substring(string1, string2):
    chars = {}
    s1 = set(string1)
    s2 = set(string2)
    for i in s1:
        chars[i] = 1
    for i in s2:
        if i in chars:
            return "YES"
    return "NO"

test1 = "hello"
test2 = "world"
print(common_substring(test1, test2))

test3 = "pants"
test4 = "color"
print(common_substring(test3, test4))