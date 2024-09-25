matrix = [[1, 2, 3],[4, 5, 6]]

transpose = []
for col in range(len(matrix[0])):
    new_row = []
    for row in range(len(matrix)):
        new_row.append(0)
    transpose.append(new_row)

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        transpose[j][i]=matrix[i][j]


print(transpose)