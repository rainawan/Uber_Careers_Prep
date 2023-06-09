"""
Raina Wan
XX-XX-XXXX

Title:
description

Time Complexity:
Space Complexity:

Technique:

Time Spent:
__ minutes

Approach:

"""


# [(A, B, "blue"), (A, C, "red"), (B, D, "blue"), (B, E, "blue"), (C, B, "red"), (D, C, "blue"), (A, D, "red"), (D, E, "red"), (E, C, "red")]

graph = {
    'A' : (['B', 'C'], 'blue')
}

print(graph['A'])
for i in graph['A'][0]:
    print(i)