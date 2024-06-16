matrix = [[x for x in input().split()] for _ in range(6)]
position = input()
row, col = int(position[1]), int(position[4])

possible_moves = {'up': (-1, 0), 'down': (1, 0), 'right': (0, 1), 'left': (0, -1)}
while True:
    commands = input().split(', ')
    if commands[0] == 'Stop':
        break
    if len(commands) == 3:
        command, direction, value = commands[0], commands[1], commands[2]
    else:
        command, direction = commands[0], commands[1]
    new_row = row + possible_moves[direction][0]
    new_col = col + possible_moves[direction][1]

    if command == 'Create':
        if matrix[new_row][new_col] == '.':
            matrix[new_row][new_col] = value
        row, col = new_row, new_col
    elif command == 'Update':
        if matrix[new_row][new_col].isalnum():
            matrix[new_row][new_col] = value
        row, col = new_row, new_col
    elif command == 'Delete':
        if matrix[new_row][new_col].isalnum():
            matrix[new_row][new_col] = '.'
        row, col = new_row, new_col
    elif command == 'Read':
        if matrix[new_row][new_col].isalnum():
            print(matrix[new_row][new_col])
        row, col = new_row, new_col

[print(*row) for row in matrix]

