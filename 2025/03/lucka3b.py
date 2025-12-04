import math

FILENAME = "2025/03/input.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

battery_amount = 12
max_joltages = []
for bank_id,bank in enumerate(INPUT):
    #print(f"{battery_amount},{len(bank)}")
    if battery_amount > len(bank):
        print("You specified a battery amount larger than the bank size...")
        break
    max_found = False

    test_number = int('9'*battery_amount)
    while not max_found:
        #print(test_number)
        str_number = str(test_number)
        digits = list(str_number)
        bad_number = False

        start_index = 0
        for i in range(battery_amount): # for the 12 batteries
            try:
                index = bank[start_index:].index(digits[i])
            except ValueError:
                test_number -= int(math.pow(10, battery_amount-1-i))    
                bad_number = True
                break

            # The if statement below is only accessed 40 times for the full input and is a bit redundant,
            # since allowing a high number that has no way of fitting enough numbers after it will eventually be dealt with
            # by the ValueError exception when the numbers after it have to look for indexes in an empty substring

            # Look at this bank for example
            # 111 111 111 911
            # When trying the combination 911 999 999 999, the first three digits will find a match but they will also set
            # the start index at the end of the bank, making it impossible to fit the rest of the numbers.
            # I thought it would save more time, but its infrequency in relation to ValueErrors makes the execution difference 
            # negligible.
            # I will keep it nonetheless for 2 reasons:
            # 1. It was the first step and key to solving part 2 today.
            # 2. I just spent all this text talking about it and I think it's interesting enough to keep.
            if index > len(bank) - (battery_amount-i):
                test_number -= int(math.pow(10, battery_amount-1-i))
                bad_number = True
                break
            else:
                start_index = start_index+index+1
        
        if bad_number:
            continue

        max_found = True
        max_joltages.append(int(''.join(digits)))

print(f"The total output joltage is {sum(max_joltages)}")