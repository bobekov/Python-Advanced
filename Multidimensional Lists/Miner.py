n = int(input())
commands = input().split()
matrix = [[x for x in input().split()] for _ in range(n)]

max_coal = 0
for row in range(n):
    for col in range(n):
        if matrix[row][col] == 's':
            curr_row, curr_col = row, col
        elif matrix[row][col] == 'c':
            max_coal += 1

sum_coal = 0
bomb = False
for command in commands:
    if command == 'up':
        if 0 <= curr_row - 1 < n:
            curr_row -= 1
    elif command == 'down':
        if 0 <= curr_row + 1 < n:
            curr_row += 1
    elif command == 'right':
        if 0 <= curr_col + 1 < n:
            curr_col += 1
    elif command == 'left':
        if 0 <= curr_col - 1 < n:
            curr_col -= 1

    if matrix[curr_row][curr_col] == 'c':
        matrix[curr_row][curr_col] = '*'
        sum_coal += 1
        if sum_coal == max_coal:
            print(f"You collected all coal! ({curr_row}, {curr_col})")
            break
    elif matrix[curr_row][curr_col] == 'e':
        print(f"Game over! {(curr_row, curr_col)}")
        bomb = True
        break

if sum_coal < max_coal and not bomb:
    print(f"{max_coal - sum_coal} pieces of coal left. ({curr_row}, {curr_col})")