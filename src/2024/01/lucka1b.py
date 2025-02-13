FILENAME = "2024/L1.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

LEFT_LIST = []
RIGHT_LIST = []
for i,ROW in enumerate(INPUT):
    TEMP = ROW.strip().split()
    LEFT_LIST.append(int(TEMP[0]))
    RIGHT_LIST.append(int(TEMP[1]))

LEFT_LIST.sort()
RIGHT_LIST.sort()

LEFT_DICT = dict()
RIGHT_DICT = dict()
for i,(a,b) in enumerate(zip(LEFT_LIST, RIGHT_LIST)):
    if a in LEFT_DICT.keys():
        LEFT_DICT[a] = LEFT_DICT[a] + 1
    else:
        LEFT_DICT[a] = 1

    if b in RIGHT_DICT.keys():
        RIGHT_DICT[b] = RIGHT_DICT[b] + 1
    else:
        RIGHT_DICT[b] = 1

SIMILARITY_SCORE = 0
for key in LEFT_DICT:
    if key not in RIGHT_DICT.keys():
        print("Missing key in right dict")
        continue

    SIMILARITY_SCORE += LEFT_DICT[key] * RIGHT_DICT[key]*key

print(SIMILARITY_SCORE)

#print("Right list:", RIGHT_LIST)
