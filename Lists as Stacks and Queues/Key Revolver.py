from collections import deque

price_bullet = int(input())
size_gun_barrel = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
value_of_intelligence = int(input())
bullets_cost = 0
shoot = 0

while bullets and locks:
    if locks[0] >= bullets[-1]:
        print('Bang!')
        bullets_cost += price_bullet
        locks.popleft()
        bullets.pop()
        shoot += 1
    else:
        bullets_cost += price_bullet
        print('Ping!')
        bullets.pop()
        shoot += 1
    if shoot == size_gun_barrel and bullets:
        print('Reloading!')
        shoot = 0

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${value_of_intelligence - bullets_cost}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")