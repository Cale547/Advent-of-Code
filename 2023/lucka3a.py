input = open("L3.txt")
answer = 0

nums = "0123456789"
symb = "*+@-&/%$#="


# first line:

line = input.readline()
lineLength = len(line)
lineUP = "."*lineLength
lineDOWN = input.readline()

iterations = 140
for row in range(iterations):#19739):
    if row == iterations-1:
        print("Fixing lineDOWN")
        lineDOWN = "."*lineLength
    part = ""
    for i in range(len(line)):
        c = line[i]
        if c in nums:
            part += c
        if part != "" and c not in nums:
            if row == 138:
                print("Row is now 138 and part is",part)

            print("Checking part",part)
            start = max(0, i-len(part)-1)
            end = min(lineLength+1, i) #start and end lets us check the machine number itself instead of looking in wrong places or getting an error
            if line[start] in symb or line[end] in symb:
                answer += int(part)
                print("Part",part,"added to sum.")
                
            else:
                for j in range(start, end+1):
                    if lineUP[j] in symb or lineDOWN[j] in symb:
                        answer += int(part)
                        print("Part",part,"added to sum.")
                        break
            part = ""
    print("Sum after row",row+1,"is",answer)
    print()
    
    lineUP = line
    line = lineDOWN
    lineDOWN = input.readline()
# each line is 141 characters long

print("Final sum is",answer)