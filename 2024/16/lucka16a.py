from PIL import Image
import os
import sys
import keyboard

slowmode = False
slowmode_counter = 0
def BFS(direction: int, row: int, col: int, visited: dict, score: int):
    global slowmode
    global slowmode_counter
    global lowest_score
    # weirdo way of letting the simulation run free for a while and then entering slowmode
    #if row == 131: 
    #    slowmode_counter += 1
    #    if slowmode_counter == 100:
    #       slowmode = True
    
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
                elif (i,j) in visited:
                    rowPrint += '!'
                else:
                    rowPrint += c
            
            terminal_print += rowPrint+'\n'
        os.system('cls')
        print(terminal_print)

    global lowest_score
    visited[(row,col)] = score
    if row == e_row and col == e_col:
        if score <= lowest_score:
            lowest_score = score
            print("\nNew record path with score",score)
        return
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
            if ((row+1,col) not in visited) or ((row+1,col) in visited and score+1001 < visited[(row+1,col)]):
                BFS(2, row+1, col, visited, score+1001)
        elif ((row+1,col) not in visited) or ((row+1,col) in visited and score+1 < visited[(row+1,col)]):
            BFS(2, row+1, col, visited, score+1)

    # going left
    if direction != 1 and left_neighbor != '#':
        if direction != 3: # turning left from up or down
            if ((row,col-1) not in visited) or ((row,col-1) in visited and score+1001 < visited[(row,col-1)]):
                BFS(3, row, col-1, visited, score+1001)
        elif ((row,col-1) not in visited) or ((row,col-1) in visited and score+1 < visited[(row,col-1)]):
            BFS(3, row, col-1, visited, score+1)


    # going up
    if direction != 2 and up_neighbor != '#':
        if direction != 0: # turning up from left or right
            if ((row-1,col) not in visited) or ((row-1,col) in visited and score+1001 < visited[(row-1,col)]):
                BFS(0, row-1, col, visited, score+1001)
        elif ((row-1,col) not in visited) or ((row-1,col) in visited and score+1 < visited[(row-1,col)]):
            BFS(0, row-1, col, visited, score+1)

    # going right
    if direction != 3 and right_neighbor != '#':
        if direction != 1: # turning right from up or down
            if ((row,col+1) not in visited) or ((row,col+1) in visited and score+1001 < visited[(row,col+1)]):
                BFS(1, row, col+1, visited, score+1001)
        elif ((row,col+1) not in visited) or ((row,col+1) in visited and score+1 < visited[(row,col+1)]):
            BFS(1, row, col+1, visited, score+1)

FILENAME = "16/L16.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

sys.setrecursionlimit(2800)
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
BFS(1, s_row, s_col, s_visit, 0)
print("Lowest score possible:",lowest_score)
