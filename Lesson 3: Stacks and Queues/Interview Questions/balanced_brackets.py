'''
Given a string made of bracket characters, determine if the string is balanced.

Ex. "{[()]}" => True
Ex. "{[(])}" => False
Ex. "{{[[(())]]}}" => True
Ex. "{[]})" => False
'''

def is_balanced(string):
    brackets = []
    for b in string:
        if b == "(" or b == "[" or b == "{":
            brackets.append(b)
        else:
            if len(brackets) == 0:
                return False
            elif b == ")" and  brackets.pop() != "(":
                return False
            elif b == "]" and brackets.pop() != "[":
                return False
            elif b == "}" and brackets.pop() != "{":
                return False
    if len(brackets) != 0:
        return False
    return True

test_1 = "{[()]}"
print(is_balanced(test_1))

test_2 = "{[(])}"
print(is_balanced(test_2))

test_3 = "{{[[(())]]}}"
print(is_balanced(test_3))

test_4 = "{[]})"
print(is_balanced(test_4))