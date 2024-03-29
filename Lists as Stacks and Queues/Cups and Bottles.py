from collections import deque

cup_capacity_litter = deque([int(x) for x in input().split()])
bottle_capacity_litter = [int(x) for x in input().split()]
bottle = 0
wasted_water = 0

while bottle_capacity_litter and cup_capacity_litter:
    if cup_capacity_litter[0] <= bottle_capacity_litter[-1]:
        wasted_water += bottle_capacity_litter[-1] - cup_capacity_litter[0]
        cup_capacity_litter.popleft()
        bottle_capacity_litter.pop()
    else:
        cup_capacity_litter[0] -= bottle_capacity_litter[-1]
        bottle_capacity_litter.pop()

if not cup_capacity_litter:
    print(f"Bottles: {' '.join([str(x) for x in bottle_capacity_litter])}")
else:
    print(f"Cups: {' '.join([str(x) for x in cup_capacity_litter])}")
print(f"Wasted litters of water: {wasted_water}")