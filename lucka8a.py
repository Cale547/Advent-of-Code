MY_INPUT = open("L8.txt")
instructions = MY_INPUT.readline().strip()
MY_INPUT.readline()
print(len(instructions))
full_maps = MY_INPUT.readlines()
print(len(full_maps))
atMap = []
goLeft = []
goRight = []
for m in full_maps:
    m = (''.join(a for a in m if a.isalnum() or a == " ")).split()
    atMap.append(m[0])
    goLeft.append(m[1])
    goRight.append(m[2])

#263 LR-instruktioner gånger 762 "vägskäl" blir 200406 kombinationer. Nåt är knasigt??

instrIndex = 0
mapIndex = 0
steps = 0
current_map = atMap[0]
while current_map != "ZZZ":
    current_map = atMap[mapIndex]
    #print(current_map)
    if current_map == "JTK":
        print("Found",current_map,"again")
    if current_map == "ZZZ":
        print("Found it!")
        break
    steps += 1
    if instructions[instrIndex] == "L":
        mapIndex = atMap.index(goLeft[mapIndex])
    else: mapIndex = atMap.index(goRight[mapIndex])
    instrIndex = (instrIndex + 1) % len(instructions)
print("It took",steps,"steps to get to ZZZ.")

#print(instructions[0])



