FILENAME = "2024/L2ex.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

for i,ROW in enumerate(INPUT):
    #INPUT[i] = ROW.strip().split()
    CURRENT_ROW = ROW.strip().split()
    
    CURRENT_CHAR = CURRENT_ROW[0]
    if not (1 <= abs(CURRENT_ROW[1] - CURRENT_CHAR) <= 3):
        continue
    
    if CURRENT_ROW[1] > CURRENT_CHAR:
        ASCENDING = True
    else:
        ASCENDING = False
    
    CURRENT_CHAR = CURRENT_ROW[0]
    for CHAR in CURRENT_ROW[2:]:
        if 1 <=
    
for    