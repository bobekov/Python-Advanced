matrix = [[x for x in input().split()] for _ in range(6)]

points = 0
hits_bucket = []
for _ in range(3):
    command = input()
    coordinates = command.strip('()').split(', ')
    next_row = int(coordinates[0])
    next_col = int(coordinates[1])

    if 0 > next_row or next_row >= 6 or 0 > next_col or next_col >= 6:
        continue
    elif (next_row, next_col) in hits_bucket:
        continue
    elif matrix[next_row][next_col] == 'B':
        hits_bucket.append((next_row, next_col))
        first_row = 0
        first_col = next_col
        for _ in range(6):
            if matrix[first_row][first_col] != 'B':
                points += int(matrix[first_row][first_col])
            first_row += 1
    else:
        continue

if 100 <= points <= 199:
    print(f"Good job! You scored {points} points, and you've won Football.")
elif 200 <= points <= 299:
    print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
elif points > 300:
    print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")
else:
    print(f"Sorry! You need {100 - points} points more to win a prize.")

