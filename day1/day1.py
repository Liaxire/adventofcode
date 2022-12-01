fileInput = open("day1_input.txt")

calories = fileInput.readlines()
calories = list(map(lambda x : int(x[:-1]) if x[:-1] != '' else None, calories))
caloriesPerElf = []

currentElf = 0
for calorie in calories:
    if calorie == None:
        caloriesPerElf += [currentElf]
        currentElf = 0
    else:
        currentElf += calorie
caloriesPerElf += [currentElf]

caloriesPerElf.sort()

# Exo 1-1
print(caloriesPerElf[-1])
# Exo 1-2
print(sum(caloriesPerElf[-3:]))