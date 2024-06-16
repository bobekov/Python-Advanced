from collections import deque

milligrams_caffeine = [int(x) for x in input().split(', ')]
energy_drink = deque([int(x) for x in input().split(', ')])

total_coffeine = 0

while milligrams_caffeine and energy_drink:
    current_caffeine = milligrams_caffeine.pop()
    current_drink = energy_drink.popleft()
    multiply = current_drink * current_caffeine

    if multiply + total_coffeine <= 300:
        total_coffeine += multiply
    else:
        energy_drink.append(current_drink)
        total_coffeine -= 30
        if total_coffeine < 0:
            total_coffeine = 0

if energy_drink:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drink)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {total_coffeine} mg caffeine.")
