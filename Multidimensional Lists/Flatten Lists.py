string = input().split('|')
matrix = []
for i in range(len(string)-1, -1, -1):
    sub = string[i].split()
    for el in sub:
        matrix.append(el)

print(*matrix)