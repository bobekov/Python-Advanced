matrix = [[x for x in input().split()] for _ in range(6)]

rover_row, rover_col = None, None
for r in range(6):
    for c in range(6):
        if matrix[r][c] == 'E':
            rover_row, rover_col = r, c

possible_moves = {'up': (-1, 0), 'down': (1, 0), 'right': (0, 1), 'left': (0, -1)}
commands = input().split(', ')
water, metal, concrete = 0, 0, 0

for command in commands:
    next_row = rover_row + possible_moves[command][0]
    next_col = rover_col + possible_moves[command][1]
    if next_row < 0:
        next_row = 5
    elif next_row >= 6:
        next_row = 0
    elif next_col < 0:
        next_col = 5
    elif next_col >= 6:
        next_col = 0

    if matrix[next_row][next_col] == 'W':
        print(f"Water deposit found at {next_row, next_col}")
        rover_row, rover_col = next_row, next_col
        water += 1
    elif matrix[next_row][next_col] == 'M':
        print(f"Metal deposit found at {next_row, next_col}")
        rover_row, rover_col = next_row, next_col
        metal += 1
    elif matrix[next_row][next_col] == 'C':
        print(f"Concrete deposit found at {next_row, next_col}")
        rover_row, rover_col = next_row, next_col
        concrete += 1
    elif matrix[next_row][next_col] == 'R':
        print(f"Rover got broken at {next_row, next_col}")
        rover_row, rover_col = next_row, next_col
        break
    else:
        rover_row, rover_col = next_row, next_col

if water and metal and concrete:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")

