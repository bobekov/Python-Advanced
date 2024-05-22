rows = int(input())
matrix = [[int(col) for col in input().split() ]for _ in range(rows)]

while True:
    command = input().split()
    if command[0] == 'END':
        break
    row, col, value = [int(x) for x in command[1:]]
    if row < 0 or row >= rows or col < 0 or col >= rows:
        print('Invalid coordinates')
        continue

    if command[0] == 'Add':
        matrix[row][col] += value
    elif command[0] == 'Subtract':
        matrix[row][col] -= value

[print(*row, sep=' ') for row in matrix]