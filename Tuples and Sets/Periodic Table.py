n = int(input())

unique = set()

for _ in range(n):
    compounds = input().split()
    for el in compounds:
        unique.add(el)

print(*unique, sep='\n')