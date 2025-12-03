FILENAME = "src/2025/03/input.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

max_joltages = []
for bank in INPUT:
    found_max = False
    for i in range(9,0,-1):
        for j in range(9,0,-1):
            tens = str(i)
            ones = str(j)
            
            try:
                tens_index = bank.index(tens)
                ones_index = bank[tens_index+1:].index(ones)
            except ValueError:
                continue

            max_joltages.append(int(tens+ones))
            found_max = True
            break

        if found_max:
            break

print(f"The total output joltage is {sum(max_joltages)}")