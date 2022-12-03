winningMap1 = {
    'A' : {
        'X': 4,
        'Y': 8,
        'Z': 3
    },
    'B' : {
        'X': 1,
        'Y': 5,
        'Z': 9
    },
    'C' : {
        'X': 7,
        'Y': 2,
        'Z': 6
    }        
}
winningMap2 = {
    'A' : {
        'X': 3,
        'Y': 4,
        'Z': 8
    },
    'B' : {
        'X': 1,
        'Y': 5,
        'Z': 9
    },
    'C' : {
        'X': 2,
        'Y': 6,
        'Z': 7
    }        
}

fileInput = open("day2-input.txt")
games = fileInput.readlines()

score = 0
for line in games:
    oponent, me = line.split()
    score += winningMap1[oponent][me]
print(score)