"""My solution for day 11 of Advent of Code 2023"""

def prettyPrint(input):
    for line in input:
        print(line)


FILENAME = "L11.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()
    #f.seek(0)
    #INPUT_CLONE = f.readlines()
INPUT_CLONE = []

COLS_TO_ADD = []
for i,ROW in enumerate(INPUT):
    INPUT[i] = ROW.strip()
    INPUT_CLONE.append(ROW.strip())
    COLS_TO_ADD.append(i)
print("We start with",len(INPUT),"rows and",len(INPUT[0]),"characters per row.")
#prettyPrint(INPUT)


ROWS_ADDED = 0
GALAXY_INDEX = 1
for i,ROW in enumerate(INPUT):
    ADD_ROW = True
    for j,CHAR in enumerate(ROW):
        if CHAR == '#':
            #INPUT_CLONE[i+ROWS_ADDED] = INPUT_CLONE[i+ROWS_ADDED][:j] + str(GALAXY_INDEX) + INPUT_CLONE[i+ROWS_ADDED][j+1:]
            #GALAXY_INDEX += 1
            ADD_ROW = False
            if j in COLS_TO_ADD:
                COLS_TO_ADD.remove(j)
    if ADD_ROW:
        INPUT_CLONE.insert(i+ROWS_ADDED,"."*len(INPUT_CLONE[0]))
        ROWS_ADDED += 1

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
#prettyPrint(INPUT)


# using enumerate ends at i,j = 11,12 and gives the correct result
# using range(len(INPUT/ROW)) ends at i,j = 11,9 and fucks up
GALAXY_ROWS = []
GALAXY_COLS = []
for i,ROW in enumerate(INPUT):
    for j,COL in enumerate(ROW):
        if INPUT[i][j] != ".":
            GALAXY_ROWS.append(i)
            GALAXY_COLS.append(j)

shortestDistSum = 0
for i in range(len(GALAXY_ROWS)):
    for j in range(i+1,len(GALAXY_ROWS)):
        #print(i,j)
        shortestDistSum += abs(GALAXY_ROWS[i]-GALAXY_ROWS[j]) + abs(GALAXY_COLS[i]-GALAXY_COLS[j])
print("Sum of all shortest distances between galaxies are:",shortestDistSum)

# 105265514 is too high
# **REDACTED** is just right
# The fix was to stop changing the galaxy indicators (#) to numbers. Since larger numbers have more than one digit,
# They mess up the distance. For example, the number 422 would calculate three different series of distances, one for each digit. 