# Count the Number of Occurrences in a Python list using a For Loop

items = ['a', 'b', 'a', 'c', 'd', 'd', 'd', 'c', 'a', 'b']
counts = {}
for item in items:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1
print(counts.get('a'))

# Returns: 3
