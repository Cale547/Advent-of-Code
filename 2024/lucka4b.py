# hämta fil

# omvandla till 2d-arrayen my_input

# trim the border since A in those positions
# cannot be the middle of an X

xmasses = 0
for i,row in enumerate(my_input)[1:-1]:
    for j,col in enumerate(row)[1:-1]:
        if col != 'A':
            continue
        topLeft = my_input[i-1][j-1]
        topRight = my_input[i-1][j+1]
        botLeft = my_input[i+1][j-1]
        botRight = my_input[i+1][j+1]
        if 
        
        
        if topLeft == 'S' and botRight == 'M':
            if (topRight == 'M' and botLeft == 'S') or (topRight == 'S' and botLeft == 'M')
                xmasses += 1
                continue
        