r = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(r)]

sum_diagonal = 0

for row in range(r):
    sum_diagonal += matrix[row][row]

print(sum_diagonal)