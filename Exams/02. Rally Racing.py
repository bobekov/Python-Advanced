def is_valid(value, max_value):
    return 0 <= value < max_value


def next_move(command1, start_row1, start_col1):
    if command1 == 'up' and is_valid(start_row1 - 1, rows):
        return start_row1 - 1, start_col1
    elif command1 == 'down' and is_valid(start_row1 + 1, rows):
        return start_row1 + 1, start_col1
    elif command1 == 'right' and is_valid(start_col1 + 1, rows):
        return start_row1, start_col1 + 1
    elif command1 == 'left' and is_valid(start_col1 - 1, rows):
        return start_row1, start_col1 - 1
    return None, None


rows = int(input())
racing_number = input()
matrix = [[x for x in input().split()] for _ in range(rows)]

start_row, start_col = 0, 0
last_tunnel_row, last_tunnel_col = None, None

for r in range(rows):
    for c in range(rows):
        if matrix[r][c] == 'T':
            last_tunnel_row, last_tunnel_col = r, c

total_kilometers = 0
finish = False

while True:
    command = input()

    if command == 'End':
        matrix[start_row][start_col] = 'C'
        break
    next_row, next_col = next_move(command, start_row, start_col)
    if next_row is None or next_col is None:
        break
    elif matrix[next_row][next_col] == '.':
        total_kilometers += 10
        start_row, start_col = next_row, next_col
    elif matrix[next_row][next_col] == 'T':
        matrix[next_row][next_col] = '.'
        total_kilometers += 30
        start_row, start_col = last_tunnel_row, last_tunnel_col
        matrix[start_row][start_col] = '.'
    elif matrix[next_row][next_col] == 'F':
        matrix[next_row][next_col] = 'C'
        total_kilometers += 10
        finish = True
        break

if not finish:
    print(f"Racing car {racing_number} DNF.")
else:
    print(f"Racing car {racing_number} finished the stage!")
print(f"Distance covered {total_kilometers} km.")

for row in matrix:
    print(''.join(row))