def is_valid(value, max_value):
    return 0 <= value < max_value


def next_move(command1, boy_row1, boy_col1):
    if command1 == 'up' and is_valid(boy_row1-1, rows):
        return boy_row1-1, boy_col1
    elif command1 == 'down' and is_valid(boy_row1+1, rows):
        return boy_row1+1, boy_col1
    if command1 == 'right' and is_valid(boy_col1+1, cols):
        return boy_row1, boy_col1+1
    if command1 == 'left' and is_valid(boy_col1-1, cols):
        return boy_row1, boy_col1-1
    return None, None


rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input()] for _ in range(rows)]

boy_row, boy_col = None, None
start_row, start_col = None, None
for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == 'B':
            boy_row, boy_col = r, c
            start_row, start_col = r, c

while True:
    command = input()
    curr_row, curr_col = next_move(command, boy_row, boy_col)
    if curr_row is None or curr_col is None:
        matrix[start_row][start_col] = ' '
        print("The delivery is late. Order is canceled.")
        break
    elif matrix[curr_row][curr_col] == '*':
        continue
    elif matrix[curr_row][curr_col] == 'A':
        matrix[curr_row][curr_col] = 'P'
        boy_row, boy_col = curr_row, curr_col
        print("Pizza is delivered on time! Next order...")
        matrix[start_row][start_col] = 'B'
        break
    elif matrix[curr_row][curr_col] == 'P':
        matrix[boy_row][boy_col] = '.'
        matrix[curr_row][curr_col] = 'R'
        boy_row, boy_col = curr_row, curr_col
        print("Pizza is collected. 10 minutes for delivery.")
        continue
    if not matrix[boy_row][boy_col] == 'R':
        matrix[boy_row][boy_col] = '.'
    boy_row, boy_col = curr_row, curr_col
    matrix[boy_row][boy_col] = '.'

for row in matrix:
    print(''.join(row))
