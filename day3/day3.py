file = open("day3_input.txt")
lines = file.readlines()

# Partie 1
def findCommon1(line):
    for i in line[:len(line) // 2]:
        if i in line[len(line)//2:]:
            return i
    raise Exception()

total = 0
for line in lines:
    common = findCommon1(line)
    total += ord(common) - ord('a') + 1 if common.islower() else ord(common) - ord('A') + 27
print(total)

# Partie 2
def findCommon2(lines):
    for letter in lines[0]:
        if letter in lines[1] and letter in lines[2]:
            return letter
    raise Exception()

total = 0
for i in range(0, len(lines), 3):
    common = findCommon2(lines[i:i+3])
    total += ord(common) - ord('a') + 1 if common.islower() else ord(common) - ord('A') + 27
print(total)