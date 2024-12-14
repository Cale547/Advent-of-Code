def BFS(start_row, start_col):
    tagged.add((start_row, start_col))
    area = 1        # Number of plots in field
    current_plot = plot_map[start_row][start_col]

    if 0 < start_row: # Look up...
        if plot_map[start_row-1][start_col] != current_plot:
            missing_up.append((start_row,start_col))
        elif (start_row-1,start_col) not in tagged:
            area += BFS(start_row-1, start_col)
    else:
        missing_up.append((start_row,start_col))

    if start_col < len(plot_map[0])-1: # Look right...
        if plot_map[start_row][start_col+1] != current_plot:
            missing_right.append((start_row,start_col))
        elif (start_row,start_col+1) not in tagged:
            area += BFS(start_row, start_col+1)
    else:
        missing_right.append((start_row,start_col))
    
    if start_row < len(plot_map)-1: # Look down...
        if plot_map[start_row+1][start_col] != current_plot:
            missing_down.append((start_row,start_col))
        elif (start_row+1,start_col) not in tagged:
            area += BFS(start_row+1, start_col)
    else:
        missing_down.append((start_row,start_col))

    if 0 < start_col: # Look left...
        if plot_map[start_row][start_col-1] != current_plot:
            missing_left.append((start_row,start_col))
        elif (start_row,start_col-1) not in tagged:
            area += BFS(start_row, start_col-1)
    else:
        missing_left.append((start_row,start_col))
    
    # ...and then cross
    return area

FILENAME = "2024/L12.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

plot_map = []
for row in INPUT:
    current_row = []
    for col in row.strip():
        current_row.append(col)
    plot_map.append(current_row)

tagged = set()
total_price = 0
for i,row in enumerate(plot_map):
    for j,plot in enumerate(row):
        if (i,j) in tagged:
            continue

        missing_up = []
        missing_right = []
        missing_down = []
        missing_left = []
        print("Checking plot",plot,"at",i,j)
        res = BFS(i,j)

        missing_up.sort()
        missing_right.sort(key=lambda x: (x[1],x[0]))
        missing_down.sort()
        missing_left.sort(key=lambda x: (x[1],x[0]))

        if i == 0 and j == 0:
            print(missing_up)
            print(missing_right)
            print(missing_down)
            print(missing_left)

        up = missing_up.copy()
        right = missing_right.copy()
        down = missing_down.copy()
        left = missing_left.copy()

        sides = 4
        for k,p in enumerate(missing_up[1:],1):
            if missing_up[k][0] == missing_up[k-1][0]:
                if missing_up[k][1] == missing_up[k-1][1]+1:
                    continue
                else:
                    sides += 1
            else:
                sides += 1

        for k,p in enumerate(missing_right[1:],1):
            if missing_right[k][1] == missing_right[k-1][1]:
                if missing_right[k][0] == missing_right[k-1][0]+1:
                    continue
                else:
                    sides += 1
            else:
                sides += 1

        for k,p in enumerate(missing_down[1:],1):
            if missing_down[k][0] == missing_down[k-1][0]:
                if missing_down[k][1] == missing_down[k-1][1]+1:
                    continue
                else:
                    sides += 1
            else:
                sides += 1
        
        for k,p in enumerate(missing_left[1:],1):
            if missing_left[k][1] == missing_left[k-1][1]:
                if missing_left[k][0] == missing_left[k-1][0]+1:
                    continue
                else:
                    sides += 1
            else:
                sides += 1
        
        print("Area is",res)
        print("Sides is",sides)
        total_price += res*sides
print("Total price for all regions:", total_price)










