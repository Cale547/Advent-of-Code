input = open("L3exempel.txt")
answer = 0

nums = "0123456789"
gear = "*"

#In this exercise I will refer to the 8 characters surrounding a star as 1-8, where 1 is the upleft one and 8 is the rightdown one
#got it?


line = input.readline()
lineLength = len(line)
lineUP = "."*lineLength
lineDOWN = input.readline()

iterations = 140
for row in range(iterations):#19739):
    if row == iterations-1:
        print("Fixing lineDOWN")
        lineDOWN = "."*lineLength
    #part = ""
    for i in range(len(line)):
        c = line[i]
        if c == "*":
            numbers_found = 0
            tagged = ""
            if lineUP[i-1] in nums:
                number = ""
                j = i-1
                while line[j-1] in nums:
                    j -= 1
                while line[j] in nums: #there will be annoying edge cases with this one
                    number += line[j]
                    j += 1
                    if j == i-1:
                        tagged += "1"
                    if j == i:
                        tagged += "2"
                    if j == i:
                        tagged += "3"
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa




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