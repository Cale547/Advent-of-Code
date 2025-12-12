FILENAME = "2025/10/input.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

all_light_diagrams = []
all_buttons = []
#all_joltages = []
total_presses = 0
for i,row in enumerate(INPUT):
    row = row.strip().split(' ')
    current_light_diagram = row[0]
    
    current_light_diagram = []
    for light in row[0][1:-1]:
        state = 0 if light == '.' else 1
        current_light_diagram.append(state)
    all_light_diagrams.append(current_light_diagram)

    buttons = []
    for button in row[1:-1]:
        if ',' not in button:
            buttons.append([int(button[1])])
        else:
            buttons.append(list(map(int, button[1:-1].split(','))))
    
    #all_joltages.append(row[-1])
    
    minimal_possible = -1
    buttons_to_press = [False]*len(buttons)
    print(current_light_diagram)
    switches = [0]*len(current_light_diagram)
    while True:
        #print(f"Trying {buttons_to_press}")

        all_lights_correct = True
        for j in range(len(switches)):
            if switches[j] % 2 != current_light_diagram[j] % 2:
                all_lights_correct = False
                break
        if all_lights_correct and (buttons_to_press.count(True) < minimal_possible or minimal_possible == -1):
            minimal_possible = buttons_to_press.count(True)
            print(f"New min: {minimal_possible}")
        
        if buttons_to_press.count(False) == 0:
            break

        #press buttons
        for j,b in enumerate(buttons_to_press):
            if not buttons_to_press[j]:
                buttons_to_press[j] = True
                break
            else:
                buttons_to_press[j] = False
                continue
        switches = [0]*len(current_light_diagram)
        for i,button in enumerate(buttons):
            if buttons_to_press[i]:
                for light in button:
                    switches[light] += 1

    print(minimal_possible)
    total_presses += minimal_possible
print(total_presses)
