import re

FILENAME = "2024/L4.txt"
with open(FILENAME, encoding="UTF8") as f:
    temp_input = f.readlines()

my_input = []
for i,row in enumerate(temp_input):
    current_row = []
    for j,col in enumerate(row.strip()):
        current_row.append(col)
    my_input.append(current_row)


# trim the border since A in those positions
# cannot be the middle of an X
xmasses = 0
for i,row in enumerate(my_input[1:], 1):
    if i == len(my_input)-1:
        break
    for j,col in enumerate(row[1:], 1):
        if j == len(my_input[0])-1:
            break
        if col != 'A':
            continue
        topLeft = my_input[i-1][j-1]
        topRight = my_input[i-1][j+1]
        botLeft = my_input[i+1][j-1]
        botRight = my_input[i+1][j+1]
        testString = topLeft+topRight+botLeft+botRight
        if testString.count('M') != 2 or testString.count('S') != 2:
            continue
        #print(testString)
        if (topLeft == 'S' and botRight == 'S') or (topRight == 'S' and botLeft == 'S'):
            print("hej")
            continue

        xmasses += 1
print("Total X-MASses:",xmasses)
