MY_INPUT = open("L7.txt")
nLines = len(MY_INPUT.readlines())
MY_INPUT = open("L7.txt")
all_games = []
fiveKind = []
fourKind = []
fullHouse = []
threeKind = []
twoPair = []
onePair = []
highCard = []
GAMETYPES = [fiveKind, fourKind, fullHouse, threeKind, twoPair, onePair, highCard]

def card_sort(n):
    match n:
        case "A": return 14
        case "K": return 13
        case "Q": return 12
        case "J": return 11
        case "T": return 10
        case _:
            return int(n)

for i in range(nLines):
    all_games.append(MY_INPUT.readline().split())

for i,game in enumerate(all_games):
    hand = []
    temp = []
    for card in game[0]:
        hand.append(card)
        temp.append(card)
    game[0] = temp

#    if hand.count(hand[0]) == 5:
#        fiveKind.append(hand)
#        print("Fivekind!")
#        break

    hand.sort(key = card_sort)
    handTypes = list(dict.fromkeys(hand))
    nTypes = len(handTypes)
    #print(nTypes)

    match nTypes:
        case 1:
            fiveKind.append(game)
            #print("Fivekind added")
            continue
        case 4:
            onePair.append(game)
            #print("onePair added")
            continue
        case 5:
            highCard.append(game)
            #print("highCard added")
            continue

    firstCard = hand[0]
    if nTypes == 2:
        if hand.count(firstCard) == 4 or hand.count(firstCard) == 1:
            fourKind.append(game)
            #print("fourKind added")
        else:
            fullHouse.append(game)
            #print("fullHouse added")
        continue
    if nTypes == 3:
        typeCount = []
        for t in handTypes:
            typeCount.append(hand.count(t))
        if 3 in typeCount:
            threeKind.append(game)
            #print("threeKind added")
            continue
        twoPair.append(game)
        #print("twoPair added")

for i,gametype in enumerate(GAMETYPES):
    if len(gametype) != 0:
        match i:
            case 0: name = "all_games"
            case 1: name = "fiveKind"
            case 2: name = "fourKind"
            case 3: name = "fullHouse"
            case 4: name = "threeKind"
            case 5: name = "twoPair"
            case 6: name = "onePair"
            case 7: name = "highCard"
        print(name,"has the games:",gametype)

all_games.clear()
for gameList in GAMETYPES:
    if len(gameList) == 0: continue
    gameList = sorted(gameList, key= lambda game: [card_sort(card) for card in game[0]], reverse=True)
    for game in gameList:
        all_games.append(game)

for game in all_games:
    print(game)

ans = 0
maxRank = nLines
for i,game in enumerate(all_games):
    newWin = int(game[1])*(maxRank-i)
    print(game[1],"*",maxRank-i)

    ans += int(game[1])*(maxRank-i)
print("Total winnings is",ans)
