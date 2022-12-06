file = open("day6_input.txt")
line = file.readline()
last_four = []

def check_if_start(characters):
    if len(characters) != 4:
        return False
    for char in characters:
        if characters.count(char) > 1:
            return False
    return True

for i in range(len(line)):
    if len(last_four) == 4:
        last_four.pop(0)
    last_four.append(line[i])
    if check_if_start(last_four):
        print(i + 1)
        break
    