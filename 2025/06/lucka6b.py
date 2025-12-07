FILENAME = "2025/06/input.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

columns = []
for j in range(len(INPUT[0])):
    current_col = []
    for i,row in enumerate(INPUT):
        current_col.append(row[j])
    columns.append(current_col)

grand_total = 0
numbers = []
operand = '?'
time_to_calculate = False
for col in columns:
    if '*' in col:
        col.remove('*')
        operand = '*'
    if '+' in col:
        col.remove('+')
        operand = '+'

    if col.count(' ') == len(INPUT) or col.count('\n') == len(INPUT):
        time_to_calculate = True

    if time_to_calculate:
        if operand == '*':
            product = 1
            for num in numbers:
                product *= num
            grand_total += product
        elif operand == '+':
            sum = 0
            for num in numbers:
                sum += num
            grand_total += sum
        
        numbers = []
        operand = '?'
        time_to_calculate = False
        continue

    numbers.append(int(''.join(col).strip()))

print(f"Grand total, sum of all answers, is {grand_total}")