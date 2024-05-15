from collections import deque

working_bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

total_honey = 0

while working_bees and nectar:
    if working_bees[0] > nectar[-1]:
        nectar.pop()
    else:
        if symbols[0] == '+':
            total_honey += abs(working_bees[0] + nectar[-1])
        elif symbols[0] == '-':
            total_honey += abs(working_bees[0] - nectar[-1])
        elif symbols[0] == '*':
            total_honey += abs(working_bees[0] * nectar[-1])
        elif symbols[0] == '/' and nectar[-1] > 0:
            total_honey += abs(working_bees[0] / nectar[-1])

        working_bees.popleft()
        nectar.pop()
        symbols.popleft()

print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")