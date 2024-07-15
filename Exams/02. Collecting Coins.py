from math import floor
rows = int(input())
matrix = [[x for x in input().split()] for _ in range(rows)]

player_row, player_col = None, None
for r in range(rows):
    for c in range(rows):
        if matrix[r][c] == 'P':
            player_row, player_col = r, c
            matrix[r][c] = ''

moves = {'up': (-1, 0), 'down': (1, 0), 'right': (0, 1), 'left': (0, -1)}
coins = 0
path = [[player_row, player_col]]
while True:
    command = input()
    next_row = player_row + moves[command][0]
    next_col = player_col + moves[command][1]

    if 0 > next_row:
        next_row = rows - 1
    if next_row >= rows:
        next_row = 0
    if 0 > next_col:
        next_col = rows - 1
    if next_col >= rows:
        next_col = 0

    if matrix[next_row][next_col] == '':
        player_row, player_col = next_row, next_col
        path.append([next_row, next_col])

    elif matrix[next_row][next_col] == 'X':
        path.append([next_row, next_col])
        coins /= 2
        print(f"Game over! You've collected {floor(coins)} coins.")
        break
    else:
        number = matrix[next_row][next_col]
        coins += int(number)
        matrix[next_row][next_col] = matrix[next_row][next_col].replace(number, '')
        player_row, player_col = next_row, next_col
        path.append([next_row, next_col])

    if coins >= 100:
        print(f"You won! You've collected {coins} coins.")
        break

print("Your path:")
for el in path:
    print(el)

