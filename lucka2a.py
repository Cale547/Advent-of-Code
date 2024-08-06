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
    # print("Now checking game",gameID)
    
    allSets = entry.partition(": ")[2].split(";")


    for set in allSets:
        # print("Now checking next set")
        colors = set.split(",")

        for j in range(len(colors)):
            col = colors[j].split()
            goodGame = color_is_ok(int(col[0]),col[1])
            # print("goodGame is",goodGame)
            if not goodGame:
                # print("Illegal pull, stops checking this set.")
                break

        if not goodGame:
            # print("Illegal pull, stops checking this game.")
            break

    if not goodGame:
        print("Game",gameID,"is illegal, continues to next game.")
    else:
        print("Game",gameID,"is legal!")
        sum += gameID
input.close()
print("Sum of legal game ID:s is",sum)