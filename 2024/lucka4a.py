import re

FILENAME = "2024/L4.txt"
with open(FILENAME, encoding="UTF8") as f:
    temp_input = f.readlines()



my_input = []
for i,row in enumerate(temp_input):
    current_row = []
    for j,col in enumerate(row.strip()):
        current_row.append(col)
    my_input.append(current_row)


my_rows = []
my_cols = [""]*len(my_input[0])
for row in my_input:
    my_rows.append(''.join(row))

    for j,col in enumerate(row):
        my_cols[j] += col

#print('Rows:',my_rows)
#print('Cols:',my_cols)

my_diagonals1 = [""]*(2*len(my_input)-1)
my_diagonals2 = [""]*(2*len(my_input)-1)
start_diagonal1 = -1
start_diagonal2 = 2
for i,row in enumerate(my_input):
    start_diagonal1 += 1
    start_diagonal2 += 1
    for j,col in enumerate(row):
        my_diagonals1[start_diagonal1+j] += col
        my_diagonals2[start_diagonal2-j] += col

#print(my_diagonals1)
#print(my_diagonals2)
        

xmas_count = 0
for words in my_rows:
    xmas_count += len(re.findall("XMAS", words))
    xmas_count += len(re.findall("SAMX", words))
for words in my_cols:
    xmas_count += len(re.findall("XMAS", words))
    xmas_count += len(re.findall("SAMX", words))
for words in my_diagonals1:
    xmas_count += len(re.findall("XMAS", words))
    xmas_count += len(re.findall("SAMX", words))
for words in my_diagonals2:
    xmas_count += len(re.findall("XMAS", words))
    xmas_count += len(re.findall("SAMX", words))
print("Total occurrences:",xmas_count)