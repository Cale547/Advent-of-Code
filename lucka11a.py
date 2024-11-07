"""My solution for day 11 of Advent of Code 2023"""
FILENAME = "L11ex.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()
    f.seek(0)
    INPUT_CLONE = f.readlines()


COLS_TO_ADD = []
for i,ROW in enumerate(INPUT):
    INPUT[i] = ROW.strip()
    INPUT_CLONE[i] = ROW.strip()
    COLS_TO_ADD.append(i)
print("We start with",len(INPUT),"rows and",len(INPUT[0]),"characters per row.")


ROWS_ADDED = 0
GALAXY_INDEX = 1
for i,ROW in enumerate(INPUT):
    ADD_ROW = True
    for j,CHAR in enumerate(ROW):
        if CHAR == '#':
            print("# found at [i,j]=",i,j)
            INPUT_CLONE[i] = ROW[:j] + str(GALAXY_INDEX) + ROW[j+1:]
            GALAXY_INDEX += 1
            ADD_ROW = False
            if j in COLS_TO_ADD:
                COLS_TO_ADD.remove(j)
    if ADD_ROW:
        INPUT_CLONE.insert(i,"."*len(INPUT_CLONE[0]))
        ROWS_ADDED += 1

#########################
print(COLS_TO_ADD)      #
for ROW in INPUT_CLONE: #
    print(ROW)          #
#########################
print("GALAXY_INDEX is",GALAXY_INDEX)

INPUT = INPUT_CLONE.copy()
for i,ROW in enumerate(INPUT):
    START = 0
    TEMP = ""
    for COL in COLS_TO_ADD:
        TEMP += ROW[START:COL]
        TEMP += "."
        START = COL
    TEMP += ROW[START:]
    INPUT[i] = TEMP
print("We end with",len(INPUT),"rows and",len(INPUT[0]),"characters per row.")

