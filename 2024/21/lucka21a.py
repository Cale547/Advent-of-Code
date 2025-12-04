

def numpad_translation(code):
    instruction = ""
    current = A

    for button in code:
        if button == 'A':
            button = A
        else:
            button = int(button)

        horizontal = numpad_cols[button] - numpad_cols[current]
        vertical = numpad_rows[button] - numpad_rows[current]

        temp_instruction = ""
        if horizontal < 0:
            temp_instruction += abs(horizontal)*'<'
        elif horizontal > 0:#se:
            temp_instruction += horizontal*'>'

        if vertical < 0:
            temp_instruction += abs(vertical)*'v'
        elif vertical > 0:#se:
            temp_instruction += vertical*'^'

        if current == A or current == 0:
            instruction += temp_instruction[::-1]
        else: 
            instruction += temp_instruction
        instruction += 'A'

        current = button
    return instruction

def arrowpad_translation(instruction:str):
    new_instruction = ""
    current = A
    for button in instruction:
        if button == 'A': button = A

        horizontal = arrowpad_cols[button] - arrowpad_cols[current]
        vertical = arrowpad_rows[button] - arrowpad_rows[current]

        temp_instruction = ""
        if horizontal < 0:
            temp_instruction += abs(horizontal)*'<'
        elif horizontal > 0:#se:
            temp_instruction += horizontal*'>'

        if vertical < 0:
            temp_instruction += abs(vertical)*'v'
        elif vertical > 0:#se:
            temp_instruction += vertical*'^'
        
        if button == '<':
            new_instruction += temp_instruction
        else:
            new_instruction += temp_instruction[::-1]
        new_instruction += 'A'

        current = button
    return new_instruction

A = 100
X = -1
numpad_rows = {7:4,8:4,9:4, 4:3,5:3,6:3, 1:2,2:2,3:2, X:1,0:1,A:1}
numpad_cols = {7:1,4:1,1:1,X:1, 8:2,5:2,2:2,0:2, 9:3,6:3,3:3,A:3}
arrowpad_rows = {X:2,'^':2,A:2, '<':1,'v':1,'>':1}
arrowpad_cols = {X:1,'<':1, '^':2,'v':2, A:3,'>':3}

FILENAME = "src/2024/21/L21.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()


complexity_sum = 0
for code in INPUT:
    code = code.strip()
    
    r2_instruction = numpad_translation(code)
    r1_instruction = arrowpad_translation(r2_instruction)
    human_instruction = arrowpad_translation(r1_instruction)
    print(code, human_instruction)

    code_id = int(code.split('A')[0])
    #print(code_id, len(human_instruction))
    complexity_sum += code_id * len(human_instruction)
print("Complexity sum is",complexity_sum)

# 183916 too high
