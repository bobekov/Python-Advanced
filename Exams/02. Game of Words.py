def is_valid(value, max_value):
    return 0 <= value < max_value


def next_move(command1, player_row1, player_col1):
    if command1 == 'up' and is_valid(player_row1 - 1, rows):
        return player_row1 - 1, player_col1
    elif command1 == 'down' and is_valid(player_row1 + 1, rows):
        return player_row1 + 1, player_col1
    elif command1 == 'right' and is_valid(player_col1 + 1, rows):
        return player_row1, player_col1 + 1
    if command1 == 'left' and is_valid(player_col1 - 1, rows):
        return player_row1, player_col1 - 1
    return None, None


string = input()
rows = int(input())
matrix = [[x for x in input()] for _ in range(rows)]

player_row, player_col = None, None
for r in range(rows):
    for c in range(rows):
        if matrix[r][c] == 'P':
            player_row, player_col = r, c
            matrix[r][c] = '-'

number_commands = int(input())
for _ in range(number_commands):
    command = input()
    next_row, next_col = next_move(command, player_row, player_col)

    if next_row is None or next_col is None:
        if string:
            string = string[:-1]

    elif matrix[next_row][next_col] != '-':
        string = string + matrix[next_row][next_col]
        matrix[next_row][next_col] = '-'
        player_row, player_col = next_row, next_col

    elif matrix[next_row][next_col] == '-':
        player_row, player_col = next_row, next_col
matrix[player_row][player_col] = 'P'

print(string)
for row in matrix:
    print(''.join(row))

