'''
Determine whether or not two given strings are anagrams.

Ex. "hi" and "ih" => True
Ex. "lol" and "ooo" => False
Ex. "iceman" and "cinema" => True
Ex. "aab" and "bba" => False
'''
 
def is_anagram(a, b):
    letters_a = {}
    letters_b = {}
    if len(a) != len(b):
        return False
    for i in a:
        if i not in letters_a:
            letters_a[i] = 1
        else:
            letters_a[i] += 1
    for i in b:
        if i not in letters_b:
            letters_b[i] = 1
        else:
            letters_b[i] += 1
    for key, val in letters_a.items():
        if key not in letters_b:
            return False
        elif val != letters_b[key]:
            return False
    return True

test1 = "hi"
test2 = "ih"
print(is_anagram(test1, test2))

test3 = "lol"
test4 = "ooo"
print(is_anagram(test3, test4))

test5 = "iceman"
test6 = "cinema"
print(is_anagram(test5, test6))

test7 = "aab"
test8 = "bba"
print(is_anagram(test7, test8))