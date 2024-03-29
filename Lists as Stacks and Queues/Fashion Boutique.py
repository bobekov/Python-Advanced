clothes_box = [int(x) for x in input().split()]
capacity_rack = int(input())

racks = 0

while clothes_box:
    racks += 1
    current_rack_capacity = capacity_rack
    while clothes_box and clothes_box[-1] <= current_rack_capacity:
        current_rack_capacity -= clothes_box.pop()

print(racks)