my_input = open("L4.txt", encoding="utf-8")
total_points = 0

# Macros
#WinNumbers = 5
WinNumbers = 10


card = my_input.readline().split()
while 'Card' in card:
    winningNums = []
    matches = 0
    for c in card[2:]:
        if len(winningNums) < WinNumbers:
            winningNums.append(c)
        else:
            if c in winningNums:
                matches += 1
    if matches > 0:
        newPoints = 2**(matches-1)
        print(newPoints,"points gained on card",card[1][0])
        total_points += newPoints
    card = my_input.readline().split()
    #card = ""

print("Total points is", total_points)