matrix = [[1, 2, 3],[4, 5, 6]]

transpose = []
for col in range(len(matrix[0])):
    new_row = []
    for row in range(len(matrix)):
        new_row.append(0)
    transpose.append(new_row)
print(transpose)