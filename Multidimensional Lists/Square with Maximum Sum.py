r, c = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split(', ')] for _ in range(r)]

max_sum = 0
max_numbers = []

for row in range(r-1):
    for col in range(c-1):
        sum_num = matrix[row][col] + matrix[row][col+1] + matrix[row+1][col] + matrix[row+1][col+1]
        if sum_num > max_sum:
            max_sum = sum_num
            max_numbers = [[matrix[row][col], matrix[row][col+1]], [matrix[row+1][col], matrix[row+1][col+1]]]

print(*max_numbers[0])
print(*max_numbers[1])
print(max_sum)