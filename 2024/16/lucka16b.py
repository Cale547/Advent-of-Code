from PIL import Image
import os
import sys
import keyboard
import time

start = time.time()
slowmode = False
slowmode_counter = 0
def BFS(direction: int, row: int, col: int, visited: dict, score: int):
    global slowmode
    global lowest_score
    global nice_seats

    if slowmode:  
        while not keyboard.is_pressed('space') and not keyboard.is_pressed('z'):
            pass

        while keyboard.is_pressed('space'):
            pass
        
        terminal_print = ""
        for i,r in enumerate(maze_map):
            rowPrint = ""
            for j,c in enumerate(r):
                if i == row and j == col:
                    match direction:
                        case 0: rowPrint += "^"
                        case 1: rowPrint += ">"
                        case 2: rowPrint += "v"
                        case 3: rowPrint += "<"
                elif c == 'S' or c == 'E':
                    rowPrint += c
                elif (i,j,0) in visited or (i,j,1) in visited or (i,j,2) in visited or (i,j,3) in visited:
                    rowPrint += '!'
                else:
                    rowPrint += c
            
            terminal_print += rowPrint+'\n'
        os.system('cls')
        print(terminal_print)


    # This path is irrelevant
    if score > 74392:
        return False

    res1 = res2 = res3 = res4 = is_part_of_winning_path = False
    visited[(row,col,direction)] = score
    if row == e_row and col == e_col:
        lowest_score = min(score, lowest_score)
        if score == 74392: #11048: #7036:
            is_part_of_winning_path = True
            if (row,col) not in nice_seats:
                nice_seats.append((row,col))
        return is_part_of_winning_path
    up_neighbor = maze_map[row-1][col]
    right_neighbor = maze_map[row][col+1]
    down_neighbor = maze_map[row+1][col]
    left_neighbor = maze_map[row][col-1]

    # titta up -> gå inte ner
    # titta höger -> gå inte vänster
    # titta ner -> gå inte upp
    # titta vänster -> gå inte höger

    # going down (yelling timber)
    if direction != 0 and down_neighbor != '#':
        if direction != 2: # turning down from left or right
            if ((row+1,col,2) not in visited) or ((row+1,col,2) in visited and score+1001 <= visited[(row+1,col,2)]):
                res1 = BFS(2, row+1, col, visited, score+1001)
        elif ((row+1,col,2) not in visited) or ((row+1,col,2) in visited and score+1 <= visited[(row+1,col,2)]):
            res1 = BFS(2, row+1, col, visited, score+1)

    # going left
    if direction != 1 and left_neighbor != '#':
        if direction != 3: # turning left from up or down
            if ((row,col-1,3) not in visited) or ((row,col-1,3) in visited and score+1001 <= visited[(row,col-1,3)]):
                res2 = BFS(3, row, col-1, visited, score+1001)
        elif ((row,col-1,3) not in visited) or ((row,col-1,3) in visited and score+1 <= visited[(row,col-1,3)]):
            res2 = BFS(3, row, col-1, visited, score+1)


    # going up
    if direction != 2 and up_neighbor != '#':
        if direction != 0: # turning up from left or right
            if ((row-1,col,0) not in visited) or ((row-1,col,0) in visited and score+1001 <= visited[(row-1,col,0)]):
                res3 = BFS(0, row-1, col, visited, score+1001)
        elif ((row-1,col,0) not in visited) or ((row-1,col,0) in visited and score+1 <= visited[(row-1,col,0)]):
            res3 = BFS(0, row-1, col, visited, score+1)

    # going right
    if direction != 3 and right_neighbor != '#':
        if direction != 1: # turning right from up or down
            if ((row,col+1,1) not in visited) or ((row,col+1,1) in visited and score+1001 <= visited[(row,col+1,1)]):
                res4 = BFS(1, row, col+1, visited, score+1001)
        elif ((row,col+1,1) not in visited) or ((row,col+1,1) in visited and score+1 <= visited[(row,col+1,1)]):
            res4 = BFS(1, row, col+1, visited, score+1)
    
    is_part_of_winning_path = res1 or res2 or res3 or res4
    if is_part_of_winning_path and (row,col) not in nice_seats:
        nice_seats.append((row,col))
    return is_part_of_winning_path

FILENAME = "2024/16/L16.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

sys.setrecursionlimit(12000)
s_row = s_col = e_row = e_col = 0
maze_map = []
for i,r in enumerate(INPUT):
    current_row = []
    for j,c in enumerate(r.strip()):
        current_row.append(c)
        if c == 'S':
            s_row = i
            s_col = j
        elif c == 'E':
            e_row = i
            e_col = j
    maze_map.append(current_row)

s_visit = {}
lowest_score = 1000000
nice_seats = []

BFS(1, s_row, s_col, s_visit, 0)
print("Lowest score possible:",lowest_score)
print("Nice seats:",len(nice_seats))

stop = time.time()
print("This thing took",stop-start,"seconds.")