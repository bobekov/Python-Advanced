numbers = int(input())
occ = []

for _ in range(numbers):
    name = input()
    occ.append(name)

print('\n'.join(set(occ)))