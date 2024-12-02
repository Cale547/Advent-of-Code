FILENAME = "2024/L2.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()



SAFE_REPORTS = 0
for i,ROW in enumerate(INPUT):
    #INPUT[i] = ROW.strip().split()
    CURRENT_ROW = ROW.strip().split()
    for i,STR in enumerate(CURRENT_ROW):
        CURRENT_ROW[i] = int(STR)


    CURRENT_DAMP = []
    for val in CURRENT_ROW:
        CURRENT_DAMP.append(val)

    for i in range(len(CURRENT_ROW)):
        TRIM_DAMP = CURRENT_DAMP.copy()
        TRIM_DAMP.pop(i)
        print(TRIM_DAMP)


        CURRENT_CHAR = TRIM_DAMP[0]
        if not (1 <= abs(TRIM_DAMP[1] - TRIM_DAMP[0]) <= 3):
            print("Fail at first two")
            continue

        ASCENDING = TRIM_DAMP[1] > TRIM_DAMP[0]

        CURRENT_CHAR = TRIM_DAMP[1]
        SAFE = True
        for NEXT_CHAR in TRIM_DAMP[2:]:
            if 1 <= abs(NEXT_CHAR - CURRENT_CHAR) <= 3:
                if (NEXT_CHAR-CURRENT_CHAR < 0) != ASCENDING: # if (is Descending) != (is Ascending)
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
            print("Safe report (damp may have been used):",CURRENT_ROW)
            SAFE_REPORTS += 1
            break


print()
print("Safe reports:",SAFE_REPORTS)
