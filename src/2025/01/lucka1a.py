FILENAME = "src/2025/01/L1.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

password_sum = 0
current_number = 50
for instruction in INPUT:
    instruction = instruction.strip()
    direction = instruction[0]
    degrees = instruction[1:]
    
    if direction == 'L':
        current_number -= int(degrees)
        while current_number < 0:
            current_number += 100
    elif direction == 'R':
        current_number += int(degrees)
        while current_number > 99:
            current_number -= 100
    print(f"Turning the dial {degrees} degrees to the {direction} ends up at {current_number}")
    if current_number == 0:
        password_sum += 1
print(f"Password is {password_sum}")
