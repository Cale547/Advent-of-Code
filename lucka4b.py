# Macros
#WinNumbers = 5
#numCards = 6

WinNumbers = 10
numCards = 220

my_input = open("L4.txt", encoding="utf-8")
cards = my_input.readlines()
cardList = [1]*numCards
total_cards = len(cardList)

for i in range(numCards):
    current = cards[i].split()
    currentCopies = cardList[i]
    winningNums = []
    matches = 0
    for c in current[2:]:
        if len(winningNums) < WinNumbers:
            winningNums.append(c)
        else:
            if c in winningNums:
                matches += 1
    if matches > 0:
        total_cards += matches*currentCopies
        for j in range(matches):
            cardList[i+j+1] += currentCopies

print("Total amount of cards is", total_cards)
