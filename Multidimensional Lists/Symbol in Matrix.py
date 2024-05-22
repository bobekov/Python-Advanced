n = int(input())

matrix = []

for row in range(n):
    elements = list(input())
    matrix.append(elements)

symbol = input()
position = None

for row_index in range(n):
    if position:
        break
    for col_index in range(len(matrix[row_index])):
        current_element = matrix[row_index][col_index]
        if current_element == symbol:
            position = (row_index, col_index)
            print(position)
            break

if not position:
    print(f'{symbol} does not occur in the matrix')