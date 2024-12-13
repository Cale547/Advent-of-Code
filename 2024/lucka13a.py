import re

FILENAME = "2024/L13.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

game_rounds = int((len(INPUT)+1)/4)
total_cost = 0
for i in range(game_rounds):
    a_line = INPUT[4*i]
    b_line = INPUT[4*i+1]
    p_line = INPUT[4*i+2]
    a = list(map(int, re.findall(r'\d+', a_line)))
    b = list(map(int, re.findall(r'\d+', b_line)))
    p = list(map(int, re.findall(r'\d+', p_line)))
    possible_sols = []

    b_ans = (p[1]*a[0]-a[1]*p[0]) / (b[1]*a[0]-a[1]*b[0])
    a_ans = (b[0]*p[1]-b[1]*p[0]) / (a[1]*b[0]-a[0]*b[1])

    if (b_ans > 0 and int(b_ans)/b_ans == 1) and (a_ans > 0 and int(a_ans)/a_ans == 1):
        total_cost += int(3*a_ans+b_ans)

print("Total cost of all possible prizes is:",total_cost)