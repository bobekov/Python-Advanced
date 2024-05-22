presents_num = int(input())
row = int(input())
matrix = [[x for x in input().split()] for _ in range(row)]

nice_kids = 0
santa = []
for r in range(row):
    for c in range(row):
        if matrix[r][c] == 'S':
            santa = [r, c]
            matrix[r][c] = '-'
        elif matrix[r][c] == 'V':
            nice_kids += 1

kids_with_present = 0

while presents_num:
    command = input()
    if command == 'Christmas morning':
        break
    if command == 'up':
        santa[0] -= 1
    elif command == 'down':
        santa[0] += 1
    elif command == 'right':
        santa[1] += 1
    elif command == 'left':
        santa[1] -= 1

    if matrix[santa[0]][santa[1]] == 'X':
        matrix[santa[0]][santa[1]] = '-'
    elif matrix[santa[0]][santa[1]] == 'V':
        matrix[santa[0]][santa[1]] = '-'
        presents_num -= 1
        nice_kids -= 1
        kids_with_present += 1
    elif matrix[santa[0]][santa[1]] == 'C':
        if matrix[santa[0]-1][santa[1]] != '-':
            presents_num -= 1
            if matrix[santa[0]-1][santa[1]] == 'V':
                nice_kids -= 1
                kids_with_present += 1
            matrix[santa[0] - 1][santa[1]] = '-'
        if matrix[santa[0]+1][santa[1]] != '-':
            presents_num -= 1
            if matrix[santa[0]+1][santa[1]] == 'V':
                nice_kids -= 1
                kids_with_present += 1
            matrix[santa[0] + 1][santa[1]] = '-'
        if matrix[santa[0]][santa[1]+1] != '-':
            presents_num -= 1
            if matrix[santa[0]][santa[1] + 1] == 'V':
                nice_kids -= 1
                kids_with_present += 1
            matrix[santa[0]][santa[1] + 1] = '-'
        if matrix[santa[0]][santa[1]-1] != '-':
            presents_num -= 1
            if matrix[santa[0]][santa[1] - 1] == 'V':
                nice_kids -= 1
                kids_with_present += 1
            matrix[santa[0]][santa[1] - 1] = '-'

matrix[santa[0]][santa[1]] = 'S'

if nice_kids:
    print("Santa ran out of presents!")
[print(*row) for row in matrix]

if not nice_kids:
    print(f"Good job, Santa! {kids_with_present} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids} nice kid/s.")