from collections import deque

chocolate = [int(x) for x in input().split(', ')]
cup_milk = deque([int(x) for x in input().split(', ')])

milkshakes = 0

while chocolate and cup_milk and milkshakes < 5:
    if chocolate[-1] <= 0 and cup_milk[0] <= 0:
        chocolate.pop()
        cup_milk.popleft()
        continue
    if chocolate[-1] <= 0:
        chocolate.pop()
        continue
    if cup_milk[0] <= 0:
        cup_milk.popleft()
        continue

    if chocolate[-1] == cup_milk[0]:
        chocolate.pop()
        cup_milk.popleft()
        milkshakes += 1
    else:
        cup_milk.rotate(-1)
        chocolate[-1] -= 5

if milkshakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join([str(x) for x in chocolate]) if chocolate else 'empty'}")
print(f"Milk: {', '.join([str(x) for x in cup_milk]) if cup_milk else 'empty'}")