numbers = [2,3,4,3,5,7,2]
nonDup = []

for item in numbers:
    if item not in nonDup:
        nonDup.append(item)

print(nonDup)