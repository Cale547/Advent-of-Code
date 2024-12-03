FILENAME = "2024/L2.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()



SAFE_REPORTS = 0
for i,ROW in enumerate(INPUT):
    #INPUT[i] = ROW.strip().split()
    CURRENT_ROW = ROW.strip().split()
    for i,STR in enumerate(CURRENT_ROW):
        CURRENT_ROW[i] = int(STR)

    CURRENT_CHAR = CURRENT_ROW[0]
    if not (1 <= abs(CURRENT_ROW[1] - CURRENT_ROW[0]) <= 3):
        print("Fail at first two")
        continue

    ASCENDING = CURRENT_ROW[1] > CURRENT_ROW[0]


    CURRENT_CHAR = CURRENT_ROW[1]
    SAFE = True
    for NEXT_CHAR in CURRENT_ROW[2:]:
        if 1 <= abs(NEXT_CHAR - CURRENT_CHAR) <= 3:
            if (NEXT_CHAR < CURRENT_CHAR) != ASCENDING: # if (is Descending) != (is Ascending)
                CURRENT_CHAR = NEXT_CHAR
            else:
                print("ASC/DESC violation in",CURRENT_ROW)
                SAFE = False
                break
        else:
            print("Size of difference violation in",CURRENT_ROW)
            SAFE = False
            break
    if SAFE:
        print("Safe report:",CURRENT_ROW)
        SAFE_REPORTS += 1
print()
print("Safe reports:",SAFE_REPORTS)
