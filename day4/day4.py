file = open("day4_input.txt")
lines = file.readlines()

pairsContained = 0
overlap = 0

def convertToInt(r):
    low, high = r.split("-")
    low = int(low)
    high = int(high)
    return (low, high)

# Partie 1  
for line in lines:
    r1, r2 = line.split(",")
    r1, r2 = convertToInt(r1), convertToInt(r2)
    if r1[0] >= r2[0] and r1[1] <= r2[1]:
        pairsContained += 1
        continue
    if r2[0] >= r1[0] and r2[1] <= r1[1]:
        pairsContained += 1
print(pairsContained)

# Partie 2
for line in lines:
    r1, r2 = line.split(",")
    r1, r2 = convertToInt(r1), convertToInt(r2)
    if r1[0] >= r2[0] and r1[0] <= r2[1] or r1[1] >= r2[0] and r1[1] <= r2[1]:
        overlap += 1
        continue
    if r2[0] >= r1[0] and r2[0] <= r1[1] or r2[1] >= r1[0] and r2[1] <= r1[1]:
        overlap += 1
print(overlap)
