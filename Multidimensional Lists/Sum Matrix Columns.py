data = input().split(', ')
rows = int(data[0])
cols = int(data[1])

matrix = []

for _ in range(rows):
    elements = [int(x) for x in input().split()]
    matrix.append(elements)

for col_index in range(cols):
    sum_columns = 0
    for row_index in range(rows):
        sum_columns += matrix[row_index][col_index]

    print(sum_columns)