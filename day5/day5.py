crates = []
crates.append(['T', 'V', 'J', 'W', 'N', 'R', 'M', 'S'])
crates.append(['V', 'C', 'P', 'Q', 'J', 'D', 'W', 'B'])
crates.append(['P', 'R', 'D', 'H', 'F', 'J', 'B'])
crates.append(['D', 'N', 'M', 'B', 'P', 'R', 'F'])
crates.append(['B', 'T', 'P','R','V','H'])
crates.append(['T','P','B','C'])
crates.append(['L', 'P', 'R', 'J','B'])
crates.append(['W', 'B','Z','T','L','S','C', 'N'])
crates.append(['G', 'S', 'L'])

file = open("day5_input.txt")
lines = file.readlines()

# Partie 1
for line in lines:
    words = line.split()
    for i in range(int(words[1])):
        current_crate = crates[int(words[3]) - 1].pop(0)
        crates[int(words[5]) - 1].insert(0, current_crate)

# Partie 2
for line in lines:
    words = line.split()
    current_crates = crates[int(words[3]) - 1][0:int(words[1])]
    crates[int(words[3]) - 1] = crates[int(words[3]) - 1][int(words[1]):]
    crates[int(words[5]) - 1] = current_crates + crates[int(words[5]) - 1]

for crate in crates:
    print(crate[0], end="")