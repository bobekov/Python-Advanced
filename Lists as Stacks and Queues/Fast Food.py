from collections import deque

quantity_food = int(input())

food_order = deque([int(x) for x in input().split()])

print(max(food_order))

while food_order and food_order[0] <= quantity_food:
    quantity_food -= food_order[0]
    food_order.popleft()

if food_order:
    print(f'Orders left: ', end='')
    while food_order:
        print(f'{food_order.popleft()}', end=' ')
else:
    print('Orders complete')