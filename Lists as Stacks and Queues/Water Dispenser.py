from collections import deque

queue = deque()
quantity = int(input())

while True:
    name = input()
    if name == 'Start':
        break
    queue.append(name)

while True:
    command = input().split()
    if command[0] == 'End':
        break
    if command[0] == 'refill':
        quantity += int(command[1])
        continue
    liters = int(command[0])
    if quantity >= liters:
        name = queue.popleft()
        print(f"{name} got water")
        quantity -= liters
    else:
        name = queue.popleft()
        print(f"{name} must wait")

print(f"{quantity} liters left")