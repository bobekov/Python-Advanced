r, c = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split(', ')] for _ in range(r)]

results = 0
for r in matrix:
    results += sum(r)

print(results)
print(matrix)