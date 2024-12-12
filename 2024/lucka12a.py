def BFS(start_row, start_col):
    tagged.add((start_row, start_col))
    area = 1        # Number of plots in field
    perimeter = 0   # Number of missing neighbors/faces of a plot that do not border a neighbor
    current_plot = plot_map[start_row][start_col]

    if 0 < start_row: # Look up...
        if plot_map[start_row-1][start_col] != current_plot:
            perimeter += 1
        elif (start_row-1,start_col) not in tagged:
            result = BFS(start_row-1, start_col)
            area += result[0]
            perimeter += result[1]
    else:
        perimeter += 1

    if start_col < len(plot_map[0])-1: # Look right...
        if plot_map[start_row][start_col+1] != current_plot:
            perimeter += 1
        elif (start_row,start_col+1) not in tagged:
            result = BFS(start_row, start_col+1)
            area += result[0]
            perimeter += result[1]
    else:
        perimeter += 1
    
    if start_row < len(plot_map)-1: # Look down...
        if plot_map[start_row+1][start_col] != current_plot:
            perimeter += 1
        elif (start_row+1,start_col) not in tagged:
            result = BFS(start_row+1, start_col)
            area += result[0]
            perimeter += result[1]
    else:
        perimeter += 1

    if 0 < start_col: # Look left...
        if plot_map[start_row][start_col-1] != current_plot:
            perimeter += 1
        elif (start_row,start_col-1) not in tagged:
            result = BFS(start_row, start_col-1)
            area += result[0]
            perimeter += result[1]
    else:
        perimeter += 1
    
    # ...and then cross
    return [area,perimeter]

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
        res = BFS(i,j)
        print("Area is",str(res[0])+',', "border is",res[1])
        total_price += res[0]*res[1]
print("Total price for all regions:", total_price)
