from collections import deque

seats = input().split(', ')
first = deque([int(x) for x in input().split(', ')])
second = deque([int(x) for x in input().split(', ')])

seats_matches = []
rotation = 0

while True:
    current_first = first.popleft()
    current_second = second.pop()
    sum_num = current_first + current_second
    chr_sum_num = chr(sum_num)

    first_concat = str(current_first) + chr_sum_num
    second_concat = str(current_second) + chr_sum_num

    for seat in first_concat, second_concat:
        if seat in seats:
            seats_matches.append(seat)
            seats.remove(seat)
            break
    else:
        first.append(current_first)
        second.appendleft(current_second)
    rotation += 1

    if len(seats_matches) == 3:
        break
    if rotation == 10:
        break

print(f"Seat matches: {', '.join(seats_matches)}")
print(f"Rotations count: {rotation}")