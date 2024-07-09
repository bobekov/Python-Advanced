rows, cols = [int(x) for x in input().split(', ')]
matrix = [[x for x in input().split()] for _ in range(rows)]

santa_row, santa_col = None, None
gift = 0
for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == 'Y':
            santa_row, santa_col = r, c
            matrix[r][c] = 'x'
        elif matrix[r][c] == 'D':
            gift += 1
        elif matrix[r][c] == 'G':
            gift += 1
        elif matrix[r][c] == 'C':
            gift += 1

possible_move = {'up': (-1, 0), 'down': (1, 0), 'right': (0, 1), 'left': (0, -1)}
items = {'Christmas decorations': 0, 'Gifts': 0, 'Cookies': 0}

while gift:
    command = input()
    if command == 'End':
        matrix[santa_row][santa_col] = 'Y'
        break
    direction, steps = command.split('-')
    step = int(steps)
    next_row = santa_row + possible_move[direction][0]
    next_col = santa_col + possible_move[direction][1]

    if next_row < 0:
        next_row = rows - 1
    elif next_row >= rows:
        next_row = 0
    elif next_col < 0:
        next_col = cols - 1
    elif next_col >= cols:
        next_col = 0

    if direction == 'up':
        for _ in range(step):
            if next_row < 0:
                next_row = rows - 1
            if matrix[next_row][next_col] == 'D':
                items['Christmas decorations'] += 1
                gift -= 1
                matrix[next_row][next_col] = 'x'
            elif matrix[next_row][next_col] == 'G':
                items['Gifts'] += 1
                gift -= 1
                matrix[next_row][next_col] = 'x'
            elif matrix[next_row][next_col] == 'C':
                items['Cookies'] += 1
                gift -= 1
                matrix[next_row][next_col] = 'x'
            elif matrix[next_row][next_col] == '.':
                matrix[next_row][next_col] = 'x'
            if not gift:
                matrix[next_row][next_col] = 'Y'
                break
            if step > 1:
                next_row -= 1
            step -= 1

    elif direction == 'down':
        for _ in range(step):
            if next_row >= rows:
                next_row = 0
            if matrix[next_row][next_col] == 'D':
                items['Christmas decorations'] += 1
                gift -= 1
                matrix[next_row][next_col] = 'x'
            elif matrix[next_row][next_col] == 'G':
                items['Gifts'] += 1
                gift -= 1
                matrix[next_row][next_col] = 'x'
            elif matrix[next_row][next_col] == 'C':
                items['Cookies'] += 1
                gift -= 1
                matrix[next_row][next_col] = 'x'
            elif matrix[next_row][next_col] == '.':
                matrix[next_row][next_col] = 'x'
            if not gift:
                matrix[next_row][next_col] = 'Y'
                break
            if step > 1:
                next_row += 1
            step -= 1

    elif direction == 'right':
        for _ in range(step):
            if next_col >= cols:
                next_col = 0
            if matrix[next_row][next_col] == 'D':
                items['Christmas decorations'] += 1
                gift -= 1
                matrix[next_row][next_col] = 'x'
            elif matrix[next_row][next_col] == 'G':
                items['Gifts'] += 1
                gift -= 1
                matrix[next_row][next_col] = 'x'
            elif matrix[next_row][next_col] == 'C':
                items['Cookies'] += 1
                gift -= 1
                matrix[next_row][next_col] = 'x'
            elif matrix[next_row][next_col] == '.':
                matrix[next_row][next_col] = 'x'
            if not gift:
                matrix[next_row][next_col] = 'Y'
                break
            if step > 1:
                next_col += 1
            step -= 1

    elif direction == 'left':
        for _ in range(step):
            if next_col < 0:
                next_col = cols - 1
            if matrix[next_row][next_col] == 'D':
                items['Christmas decorations'] += 1
                gift -= 1
                matrix[next_row][next_col] = 'x'
            elif matrix[next_row][next_col] == 'G':
                items['Gifts'] += 1
                gift -= 1
                matrix[next_row][next_col] = 'x'
            elif matrix[next_row][next_col] == 'C':
                items['Cookies'] += 1
                gift -= 1
                matrix[next_row][next_col] = 'x'
            elif matrix[next_row][next_col] == '.':
                matrix[next_row][next_col] = 'x'
            if not gift:
                matrix[next_row][next_col] = 'Y'
                break
            if step > 1:
                next_col -= 1
            step -= 1

    santa_row, santa_col = next_row, next_col

if not gift:
    print("Merry Christmas!")

print("You've collected:")
for key, value in items.items():
    print(f"- {value} {key}")

for row in matrix:
    print(' '.join(row))
