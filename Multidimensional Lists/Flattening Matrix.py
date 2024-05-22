r = int(input())
matrix = [[int(x) for x in input().split(', ')] for _ in range(r)]
flattened = []

for row in matrix:
    for num in row:
        flattened.append(num)

print(flattened)