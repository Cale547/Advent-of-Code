FILENAME = "2025/06/input.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

problems_grid = []
for row in INPUT:
    row = row.strip().split(' ')
    while '' in row:
        row.remove('')
    problems_grid.append(row)

problems = []
for j in range(len(problems_grid[0])):
    current_col = []
    for i in range(len(problems_grid)):
        current_col.append(problems_grid[i][j])
    problems.append(current_col)

grand_total = 0
for i,problem in enumerate(problems):
    operation = problem[-1]
    current_result = -1
    if operation == '+':
        current_result = 0
        for term in problem[0:len(problem)-1]:
            current_result += int(term)
    elif operation == '*':
        current_result = 1
        for factor in problem[0:len(problem)-1]:
            current_result *= int(factor)
    
    if current_result == -1:
        print("oops")
    grand_total += current_result

print(f"Grand total, sum of all answers, is {grand_total}")