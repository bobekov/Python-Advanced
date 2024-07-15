first, second = input().split(', ')
matrix = [[x for x in input().split()] for _ in range(7)]

first_score, second_score = 501, 501
first_win, second_win = False, False
fist_throws, second_throws = 0, 0
while True:
    first_coordinates = input().strip('()').split(', ')
    first_row, first_col = int(first_coordinates[0]), int(first_coordinates[1])
    fist_throws += 1
    if 0 > first_row >= 7 or 0 > first_col >= 7:
        continue
    elif matrix[first_row][first_col] == 'D':
        first_score -= (int(matrix[first_row][0]) + int(matrix[first_row][-1]) + int(matrix[0][first_col]) + int(matrix[-1][first_col])) * 2
    elif matrix[first_row][first_col] == 'T':
        first_score -= (int(matrix[first_row][0]) + int(matrix[first_row][-1]) + int(matrix[0][first_col]) + int(matrix[-1][first_col])) * 3
    elif matrix[first_row][first_col] == 'B':
        first_win = True
        break
    else:
        first_score -= int(matrix[first_row][first_col])
    if first_score <= 0:
        first_win = True
        break

    second_coordinates = input().strip('()').split(', ')
    second_row, second_col = int(second_coordinates[0]), int(second_coordinates[1])
    second_throws += 1
    if 0 > second_row >= 7 or 0 > second_col >= 7:
        continue
    elif matrix[second_row][second_col] == 'D':
        second_score -= (int(matrix[second_row][0]) + int(matrix[second_row][-1]) + int(matrix[0][second_col]) + int(matrix[-1][second_col])) * 2
    elif matrix[second_row][second_col] == 'T':
        second_score -= (int(matrix[second_row][0]) + int(matrix[second_row][-1]) + int(matrix[0][second_col]) + int(matrix[-1][second_col])) * 3
    elif matrix[second_row][second_col] == 'B':
        second_win = True
        break
    else:
        second_score -= int(matrix[second_row][second_col])
    if second_score <= 0:
        second_win = True
        break

if first_win:
    print(f"{first} won the game with {fist_throws} throws!")
if second_win:
    print(f"{second} won the game with {second_throws} throws!")

