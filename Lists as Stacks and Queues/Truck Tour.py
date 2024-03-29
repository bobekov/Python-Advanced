from collections import deque

number_pumps = int(input())

pumps = deque()
start_position = 0
stops = 0

for _ in range(number_pumps):
    amount_petrol, distance = input().split()
    pumps.append([int(amount_petrol), int(distance)])

while stops < number_pumps:
    fuel = 0
    for i in range(number_pumps):
        fuel += pumps[i][0]
        destination = pumps[i][1]
        if fuel < destination:
            pumps.rotate(-1)
            start_position += 1
            stops = 0
            break
        fuel -= destination
        stops += 1

print(start_position)