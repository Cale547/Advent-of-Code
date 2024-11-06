INPUT = open("L9.txt").readlines()
lines = []
FINAL_ANS = 0

for line in INPUT:
    line = line.strip().split()
    temp = []
    for n in line:
        temp.append(int(n))
    temp.reverse()
    lines.append(temp)

print(lines)

for baseLine in lines:
    hopLines = [baseLine]

    currentLine = baseLine
    while True:
        newLine = []
        for i in range(1,len(currentLine)):
            newLine.append(currentLine[i-1]-currentLine[i])
        hopLines.append(newLine)

        if sum(newLine) != 0:
            currentLine = newLine
        else:
            break

    hopLines.reverse() # Will reverse the list so it starts with the zero-list
    print(hopLines)

    toAdd = 0
    for i, vals in enumerate(hopLines):
        vals.append(vals[-1] - toAdd)
        toAdd = vals[-1]
    FINAL_ANS += hopLines[-1][-1]
    #print(FINAL_ANS)
    #print(hopLines)


    # AI will take over works
    # maoney on your accånt
    # If it's funny at work
print(FINAL_ANS)
