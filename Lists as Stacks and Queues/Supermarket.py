from collections import deque

queue = deque()

while True:
    name = input()
    if name == 'End':
        break

    if name == 'Paid':
        print('\n'.join(queue))
        queue.clear()
        continue

    queue.append(name)

print(f'{len(queue)} people remaining.')