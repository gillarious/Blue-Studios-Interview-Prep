'''
You are given a string with A and B characters. Find the minimum number 
of required deletions so that there are only alternating characters.

Ex. AABAAB => 2
'''

def alternating_characters(string):
    deletion = 0
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            deletion += 1
    return deletion

test = "AABAAB"
print(alternating_characters(test))