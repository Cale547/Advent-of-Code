"""My solution for day 11 of Advent of Code 2023"""

def prettyPrint(input):
    for line in input:
        print(line)


FILENAME = "L11.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

COLS_TO_ADD = []
for i,ROW in enumerate(INPUT):
    INPUT[i] = ROW.strip()
    COLS_TO_ADD.append(i) # This would not work if the input wasn't square. To fix, just iterate through rows methinks
print("We start with",len(INPUT),"rows and",len(INPUT[0]),"characters per row.")
#prettyPrint(INPUT)


GALAXY_ROWS = []
GALAXY_COLS = []
ROWS_TO_ADD = []
for i,ROW in enumerate(INPUT):
    ADD_ROW = True
    for j,CHAR in enumerate(ROW):
        if CHAR == '#':
            GALAXY_ROWS.append(i)
            GALAXY_COLS.append(j)
            ADD_ROW = False
            if j in COLS_TO_ADD:
                COLS_TO_ADD.remove(j)
    if ADD_ROW:
        ROWS_TO_ADD.append(i)

# using enumerate ends at i,j = 11,12 and gives the correct result
# using range(len(INPUT/ROW)) ends at i,j = 11,9 and fucks up

print("We end with",len(INPUT)+len(ROWS_TO_ADD),"rows and",len(INPUT[0])+len(COLS_TO_ADD),"characters per row.")
#prettyPrint(INPUT)

EXTRA_SPACE = 1000000 - 1
shortestDistSum = 0
nGalaxies = len(GALAXY_ROWS)
for i in range(nGalaxies):
    for j in range(i+1,nGalaxies):
        ROWS_APART = 0
        COLS_APART = 0
        for row in ROWS_TO_ADD:
            if (GALAXY_ROWS[i] < row < GALAXY_ROWS[j]) or (GALAXY_ROWS[j] < row < GALAXY_ROWS[i]):
                ROWS_APART += 1
        for col in COLS_TO_ADD:
            if (GALAXY_COLS[i] < col < GALAXY_COLS[j]) or (GALAXY_COLS[j] < col < GALAXY_COLS[i]):
                COLS_APART += 1

        

        shortestDistSum += abs(GALAXY_ROWS[i]-GALAXY_ROWS[j]) + abs(GALAXY_COLS[i]-GALAXY_COLS[j]) + EXTRA_SPACE*(ROWS_APART+COLS_APART)
print("Sum of all shortest distances between galaxies are:",shortestDistSum)


# 105265514 is too high
# **REDACTED** is just right
# The fix was to stop changing the galaxy indicators (#) to numbers. Since larger numbers have more than one digit,
# They mess up the distance. For example, the number 422 would calculate three different series of distances, one for each digit. 