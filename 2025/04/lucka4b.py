FILENAME = "2025/04/input.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

accessible_rolls = 0

roll_map = []
roll_map_copy = []
for row in INPUT:
    roll_map.append(row)
    roll_map_copy.append(row)

new_rolls = True
while new_rolls:
    new_rolls = False
    for i,row in enumerate(roll_map):
        for j,col in enumerate(row):
            if roll_map[i][j] != '@':
                continue

            adjacent_rolls = 0
            for i2 in range(-1,2):
                for j2 in range(-1,2):
                    if i2 == 0 and j2 == 0:
                        continue
                    if 0 <= i+i2 <= (len(roll_map)-1) and 0 <= j+j2 <= (len(row)-1):
                        if roll_map[i+i2][j+j2] == '@':
                            adjacent_rolls += 1
            if adjacent_rolls < 4:
                new_rolls = True
                accessible_rolls += 1
                roll_map_copy[i] = (roll_map_copy[i][0:j] + '.' + roll_map_copy[i][j+1:])

    print(f"Total rolls removed this iteration: {accessible_rolls}")
    for i,row in enumerate(roll_map_copy):
        row_copy = ""
        for col in row:
            row_copy += col
        roll_map[i] = row_copy

print(f"There are {accessible_rolls} accessible paper rolls")