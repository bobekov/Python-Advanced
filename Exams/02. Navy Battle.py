rows = int(input())
matrix = [[x for x in input()] for _ in range(rows)]

submarine_row, submarine_col = None, None
cruiser = 0
for r in range(rows):
    for c in range(rows):
        if matrix[r][c] == 'S':
            submarine_row, submarine_col = r, c
            matrix[submarine_row][submarine_col] = '-'
        elif matrix[r][c] == 'C':
            cruiser += 1

damage = 0
while True:
    command = input()
    new_row, new_col = None, None
    if command == 'up':
        new_row, new_col = submarine_row - 1, submarine_col
    elif command == 'down':
        new_row, new_col = submarine_row + 1, submarine_col
    elif command == 'right':
        new_row, new_col = submarine_row, submarine_col + 1
    elif command == 'left':
        new_row, new_col = submarine_row, submarine_col - 1

    if matrix[new_row][new_col] == '*':
        matrix[new_row][new_col] = '-'
        submarine_row, submarine_col = new_row, new_col
        damage += 1
    elif matrix[new_row][new_col] == 'C':
        matrix[new_row][new_col] = '-'
        submarine_row, submarine_col = new_row, new_col
        cruiser -= 1
    elif matrix[new_row][new_col] == '-':
        submarine_row, submarine_col = new_row, new_col

    if cruiser == 0:
        matrix[new_row][new_col] = 'S'
        print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        break
    if damage == 3:
        matrix[new_row][new_col] = 'S'
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{new_row}, {new_col}]!")
        break

for row in matrix:
    print(''.join(row))