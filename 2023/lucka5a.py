my_input = open("L5.txt", encoding="utf-8")

# Information
# Line number ex = 33
# Line number real = 248
# Seed length ex = 4

seeds = []
lines = my_input.readlines()

for num in lines[0].split()[1:]:
    seeds.append(int(num))
nextSeeds = seeds

print("Starting seeds:")
for i in range(1, 248):
    currentLine = lines[i].split()
    if len(currentLine) == 0:
        #print("Boring line, passing.")
        continue
    if "map:" in currentLine:
        for i, seed in enumerate(seeds):
            if nextSeeds[i] != 0:
                seeds[i] = nextSeeds[i]

        nextSeeds = [0]*len(seeds)
        print(seeds)
        print("Seeds after",currentLine[0],currentLine[1])
        continue

    currentLine = [int(stringNumber) for stringNumber in currentLine]
    startDestination = currentLine[0]
    startSource = currentLine[1]
    mapLength = currentLine[2]

    for s, DONTUSE in enumerate(seeds):
        if nextSeeds[s] != 0: #If the seed in this spot has already been mapped, we don't use the new value to remap it
            continue
        minimumSource = (seeds[s] - mapLength) + 1
        if startSource < minimumSource or startSource > seeds[s]:
            continue

        nextSeeds[s] = startDestination + (seeds[s]-startSource)

# Last copy from nextSeeds:
for i, seed in enumerate(seeds):
    if nextSeeds[i] != 0:
        seeds[i] = nextSeeds[i]

print(seeds)
print(min(seeds))
