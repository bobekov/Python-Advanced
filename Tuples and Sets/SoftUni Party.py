n = int(input())

list_guest = set()

for _ in range(n):
    guest = input()
    list_guest.add(guest)

while True:
    guest = input()
    if guest == 'END':
        break
    elif guest in list_guest:
        list_guest.remove(guest)

print(len(list_guest))

for num in sorted(list_guest):
    print(num)