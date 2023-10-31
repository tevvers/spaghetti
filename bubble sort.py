names = ["Henry", "Steve", "Julie", "Ava", "Tom", "Olivia"]
numitems = len(names)
for i in range(numitems -1):
    for j in range(numitems - 1 - i):
        if names[j] > names[j+1]:
            names[j], names[j+1] = names[j+1], names[j]
        print(names)
print(names)