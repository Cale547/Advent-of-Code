FILENAME = "src/2025/01/L1.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

password_sum = 0
current_number = 50
for instruction in INPUT:
    instruction = instruction.strip()
    direction = instruction[0]
    degrees = int(instruction[1:])
    print(f"Turning the dial {instruction}")
    start_number = current_number

    if direction == 'L':
        current_number -= degrees
        while current_number < 0:
            if start_number != 0:
                print("adding 1 while current_num < 0")
                password_sum += 1
            current_number += 100
            start_number = current_number

    elif direction == 'R':
        current_number += degrees
        while current_number > 99:
            current_number -= 100
            if current_number != 0:
                print("adding 1 while current_num > 99")
                password_sum += 1

    print(f"We end up at {current_number}")
    if current_number == 0:
        print("adding 1 because current_num = 0")
        password_sum += 1
    print()
print(f"Password is {password_sum}")
