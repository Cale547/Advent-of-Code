FILENAME = "2025/10/input.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

all_light_diagrams = []
all_buttons = []
#all_joltages = []
total_presses = 0
for i,row in enumerate(INPUT):
    row = row.strip().split(' ')    
    current_light_diagram = []
    for light in row[0][1:-1]:
        state = False if light == '.' else True
        current_light_diagram.append(state)
    all_light_diagrams.append(current_light_diagram)

    current_buttons = []
    for button in row[1:-1]:
        if ',' not in button:
            current_buttons.append([int(button[1])])
        else:
            current_buttons.append(list(map(int, button[1:-1].split(','))))
    all_buttons.append(current_buttons)
    
    #all_joltages.append(row[-1])
    
    minimal_possible = -1
    buttons_to_press = [False]*len(current_buttons)
    turned_on_lights = [False]*len(current_light_diagram)
    while True:
        all_lights_correct = True
        for j in range(len(turned_on_lights)):
            if turned_on_lights[j] != current_light_diagram[j]:
                all_lights_correct = False
                break
        active_buttons_count = buttons_to_press.count(True)
        if all_lights_correct and (active_buttons_count < minimal_possible or minimal_possible == -1):
            minimal_possible = active_buttons_count
            #print(f"New min: {minimal_possible}")
        
        # Last iteration will try pressing all buttons which means no buttons are False
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
        
        turned_on_lights = [False]*len(current_light_diagram)
        for i,button in enumerate(current_buttons):
            if buttons_to_press[i]:
                for light in button:
                    turned_on_lights[light] = not turned_on_lights[light]

    total_presses += minimal_possible
print(f"The fewest button presses required to correctly configure the indicator lights on all of the machines is {total_presses}")
