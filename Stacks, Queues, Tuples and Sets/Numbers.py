first = set(int(x) for x in input().split())
second = set(int(x) for x in input().split())
n = int(input())

for _ in range(n):
    line = input().split()
    command = line[0] + ' ' + line[1]
    numbers = [int(num) for num in line[2:]]
    if command == 'Add First':
        first.update(numbers)
    elif command == 'Add Second':
        second.update(numbers)
    elif command == 'Remove First':
        first.difference_update(numbers)
    elif command == 'Remove Second':
        second.difference_update(numbers)
    elif command == 'Check Subset':
        print(first.issubset(second) or second.issubset(first))

print(*sorted(first), sep=', ')
print(*sorted(second), sep=', ')