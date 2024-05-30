def is_valid(value, max_value):
    return 0 <= value < max_value


def next_move(command1, square_row1, square_col1):
    if command1 == 'up' and is_valid(square_row1-1, rows):
        return square_row1-1, square_col1
    elif command1 == 'down' and is_valid(square_row1+1, rows):
        return square_row1+1, square_col1
    elif command1 == 'right' and is_valid(square_col1+1, rows):
        return square_row1, square_col1+1
    elif command1 == 'left' and is_valid(square_col1-1, rows):
        return square_row1, square_col1-1
    return None, None


rows = int(input())
commands = input().split(', ')
matrix = [[x for x in input()] for _ in range(rows)]

square_row, square_col = None, None
total_hazelnuts = 0
for r in range(rows):
    for c in range(rows):
        if matrix[r][c] == 's':
            square_row, square_col = r, c
        elif matrix[r][c] == 'h':
            total_hazelnuts += 1

hazelnuts = 0
trap = False
out = False
for command in commands:
    current_row, current_col = next_move(command, square_row, square_col)
    if current_row is None or current_col is None:
        print("The squirrel is out of the field.")
        out = True
        break
    elif matrix[current_row][current_col] == 'h':
        hazelnuts += 1
        total_hazelnuts -= 1
        matrix[current_row][current_col] = '*'
        square_row, square_col = current_row, current_col
        if hazelnuts == 3:
            break
    elif matrix[current_row][current_col] == '*':
        square_row, square_col = current_row, current_col
    elif matrix[current_row][current_col] == 't':
        print("Unfortunately, the squirrel stepped on a trap...")
        trap = True
        break

if not total_hazelnuts:
    print("Good job! You have collected all hazelnuts!")
elif total_hazelnuts and not trap and not out:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")