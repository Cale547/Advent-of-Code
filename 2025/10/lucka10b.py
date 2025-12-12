FILENAME = "2025/10/input.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

all_light_diagrams = []
all_buttons = []
all_joltages = []
total_presses = 0
for i,row in enumerate(INPUT):
    print(i)
    row = row.strip().split(' ')    
    current_light_diagram = []
    for light in row[0][1:-1]:
        state = 0 if light == '.' else 1
        current_light_diagram.append(state)
    all_light_diagrams.append(current_light_diagram)

    current_buttons = []
    for button in row[1:-1]:
        if ',' not in button:
            current_buttons.append([int(button[1])])
        else:
            current_buttons.append(list(map(int, button[1:-1].split(','))))
    
    joltage_requirements = row[-1]
    current_joltages = list(map(int, joltage_requirements[1:-1].split(',')))
    all_joltages.append(current_joltages)
    #print(current_joltages)
    
    minimal_possible = -1
    buttons_to_press = [0]*len(current_buttons)
    
    maxes = []
    for button in current_buttons:
        limit = -1
        for index in button:
            if current_joltages[index] < limit or limit == -1:
                maxes.append(current_joltages[index])
                break
    
    #print(maxes)

    switches = [0]*len(current_joltages)
    while True:
        #print(f"Trying {buttons_to_press}")

        all_joltages_correct = True
        for j in range(len(switches)):
            #print(f"switches[j]={switches[j]}, current_joltages[j]={current_joltages[j]}")
            if switches[j] != current_joltages[j]:
                all_joltages_correct = False
                break

        active_buttons_count = sum(buttons_to_press)
        if all_joltages_correct and (active_buttons_count < minimal_possible or minimal_possible == -1):
            minimal_possible = active_buttons_count
            print(f"New min: {minimal_possible}")
        
        # does this work?
        if buttons_to_press == maxes:
            break

        #press buttons
        for j,b in enumerate(buttons_to_press):
            if buttons_to_press[j] < maxes[j]:
                buttons_to_press[j] += 1
                break
            else:
                buttons_to_press[j] = 0
                continue
        if minimal_possible != -1 and sum(buttons_to_press) >= minimal_possible:
            continue

        switches = [0]*len(current_light_diagram)
        for i,button in enumerate(current_buttons):
            for counter in button:
                switches[counter] += buttons_to_press[i]

    #print(minimal_possible)
    total_presses += minimal_possible
print(total_presses)
