def color_is_ok(amount, color):
    if color == "red" and amount > 12:
        return False
    elif color == "green" and amount > 13:
        return False
    elif color == "blue" and amount > 14:
        return False
    else:
        return True
    


# partition
# 12 red
# 13 green
# 14 blue

input = open("L2.txt")
sum = 0

for i in range(100):
    entry = input.readline()
    gameID = i + 1
    numberOfSets = entry.count(";") + 1
    
    allSets = entry.partition(": ")[2].split(";")

    minR = 0
    minG = 0
    minB = 0

    for set in allSets:
        colors = set.split(",")

        for j in range(len(colors)):
            col = colors[j].split()
            # int(col[0]) == amount
            # col[1] == color
            amount = int(col[0])
            if col[1] == "red" and amount > minR:
                minR = amount
            if col[1] == "green" and amount > minG:
                minG = amount
            if col[1] == "blue" and amount > minB:
                minB = amount
    
    power = minR*minG*minB
    sum += power

input.close()
print("Sum of minimum cube set power is",sum)