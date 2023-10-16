temperature = [0,16,32,10,5,3,2,5,7,2345,5,4,5,5,3,435,5,5,34,345,5,435,345,435,345,345,435,35,45,43,5,345,354,5,44,3,3,45,435,34,53,45,345,345,5,2,2,6,354,5]

bandA = 0
bandB = 0
bandC = 0
bandD = 0

for i in temperature:
    if i <= 10:
        bandA += 1
    if i >= 11 and i <= 20:
        bandB += 1
    if i >= 21 and i <= 30:
        bandC += 1
    if i >= 31:
        bandD += 1

print("Band A: ", bandA)
print("Band B: ", bandB)
print("Band C: ", bandC)
print("Band D: ", bandD,'\n')

temperature.sort()
print(temperature)