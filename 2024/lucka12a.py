def BFS(start_row, start_col):
    

# get input

global plot_map = []
for row in INPUT:
    current_row = []
    for col in row.strip():
        current_row.append(col)
    plot_map.append(current_row)

global tagged = set()
for i,row in enumerate(plot_map):
    for j,plot in enumerate(row):
        if (i,j) in tagged:
            continue
        BFS(i,j, plot_map)