import time

def blink(stone, blinks, tagged):
    #print("Blinking at stone engraved with",stone,"with",blinks,"blinks left.")
    if str(stone)+','+str(blinks) in tagged.keys():
        return tagged[str(stone)+','+str(blinks)]

    stone_count = 1
    digits = len(stone)
    if blinks == 0:
        return stone_count

    if int(stone) == 0:
        stone_count -= 1
        stone_count += blink('1',blinks-1, tagged)

    elif digits % 2 == 0:
        stone_count -= 1
        half = int(digits/2)
        stone1 = str(int(stone[:half])) # Removes leading zeroes from stones
        stone2 = str(int(stone[half:])) 

        stone_count += blink(stone1, blinks-1, tagged) + blink(stone2, blinks-1, tagged)

    else:
        stone_count -= 1
        new_stone = str(int(stone)*2024)
        stone_count += blink(new_stone, blinks-1, tagged)

    tagged[str(stone)+','+str(blinks)] = stone_count
    return stone_count

start = time.time()

FILENAME = "2024/L11.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

rock_map = INPUT[0].split()

rocks_found = 0
mapped = {}
for rock in rock_map:
    rocks_found += blink(rock, 300, mapped)

print("In the final line,",rocks_found,"rocks lie.")
stop = time.time()
print("This took",stop-start,"seconds")