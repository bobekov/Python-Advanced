n = int(input())
matrix = [[x for x in input()] for _ in range(n)]

snake_row, snake_col = None, None
lair_row, lair_col = None, None
for r in range(n):
    for c in range(n):
        if matrix[r][c] == 'S':
            snake_row, snake_col = r, c
            matrix[r][c] = '.'
        elif matrix[r][c] == 'B':
            lair_row, lair_col = r, c

moves = {'up': (-1, 0), 'down': (1, 0), 'right': (0, 1), 'left': (0, -1)}
food = 0
while True:
    command = input()
    next_row = snake_row + moves[command][0]
    next_col = snake_col + moves[command][1]

    if 0 > next_row or next_row >= n or 0 > next_col or next_col >= n:
        print("Game over!")
        break
    elif matrix[next_row][next_col] == '*':
        food += 1
        matrix[next_row][next_col] = '.'
        snake_row, snake_col = next_row, next_col
    elif matrix[next_row][next_col] == 'B':
        matrix[next_row][next_col] = '.'
        snake_row, snake_col = lair_row, lair_col
        matrix[snake_row][snake_col] = '.'
    else:
        matrix[next_row][next_col] = '.'
        snake_row, snake_col = next_row, next_col

    if food == 10:
        matrix[next_row][next_col] = 'S'
        print("You won! You fed the snake.")
        break

print(f"Food eaten: {food}")
for row in matrix:
    print(''.join(row))
