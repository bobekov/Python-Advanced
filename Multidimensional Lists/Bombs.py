def is_valid(row, col):
    return 0 <= row < n and 0 <= col < n


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
bomb_coordinates = list(map(lambda x: tuple(map(int, x.split(','))), input().split()))

for row, col in bomb_coordinates:
    if is_valid(row, col) and matrix[row][col] > 0:
        damage = matrix[row][col]
        matrix[row][col] = 0

        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if is_valid(r, c) and matrix[r][c] > 0:
                    matrix[r][c] -= damage

alive_cells_count = 0
sum_of_cells = 0

for row in matrix:
    for cell in row:
        if cell > 0:
            alive_cells_count += 1
            sum_of_cells += cell

print(f"Alive cells: {alive_cells_count}")
print(f"Sum: {sum_of_cells}")

[print(*row) for row in matrix]