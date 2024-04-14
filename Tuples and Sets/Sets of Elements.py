n, m = [int(x) for x in input().split()]
n1 = set()
m1 = set()

for _ in range(n):
    n1.add(int(input()))
for _ in range(m):
    m1.add(int(input()))

result = n1 & m1
print(*result, sep='\n')