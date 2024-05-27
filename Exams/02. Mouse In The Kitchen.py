def is_valid(value, max_value):
    return 0 <= value < max_value


def next_move(command1, mouse_row1, mouse_col1):
    if command1 == 'up' and is_valid(mouse_row1-1, rows):
        return mouse_row1-1, mouse_col1
    elif command1 == 'down' and is_valid(mouse_row1+1, rows):
        return mouse_row1+1, mouse_col1
    elif command1 == 'right' and is_valid(mouse_col1+1, cols):
        return mouse_row1, mouse_col1+1
    elif command1 == 'left' and is_valid(mouse_col1-1, cols):
        return mouse_row1, mouse_col1-1
    return None, None


rows, cols = [int(x) for x in input().split(',')]
matrix = [[x for x in input()] for _ in range(rows)]

mouse_row, mouse_col = None, None
cheese = 0
for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == 'M':
            mouse_row = r
            mouse_col = c
        elif matrix[r][c] == 'C':
            cheese += 1

while True:
    command = input()
    if command == 'danger':
        break
    next_row, next_col = next_move(command, mouse_row, mouse_col)
    if next_row is None or next_col is None:
        print("No more cheese for tonight!")
        break
    elif matrix[next_row][next_col] == '*':
        matrix[mouse_row][mouse_col] = '*'
        mouse_row, mouse_col = next_row, next_col
        matrix[mouse_row][mouse_col] = 'M'
    elif matrix[next_row][next_col] == 'C':
        matrix[mouse_row][mouse_col] = '*'
        mouse_row, mouse_col = next_row, next_col
        matrix[mouse_row][mouse_col] = 'M'
        cheese -= 1
        if not cheese:
            print("Happy mouse! All the cheese is eaten, good night!")
            break
    elif matrix[next_row][next_col] == 'T':
        matrix[mouse_row][mouse_col] = '*'
        mouse_row, mouse_col = next_row, next_col
        matrix[mouse_row][mouse_col] = 'M'
        print("Mouse is trapped!")
        break
    elif matrix[next_row][next_col] == '@':
        continue

if cheese and command == 'danger':
    print("Mouse will come back later!")
for row in matrix:
    print(''.join(row))
