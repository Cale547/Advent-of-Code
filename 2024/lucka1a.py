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
#print("Left list:", LEFT_LIST)
#print("Right list:", RIGHT_LIST)

TOTAL_DIST = 0
for i,(a,b) in enumerate(zip(LEFT_LIST, RIGHT_LIST)):
    TOTAL_DIST += abs(a-b)

print("Total distance:",TOTAL_DIST)