from collections import deque

firework = deque([int(x) for x in input().split(', ')])
power = [int(x) for x in input().split(', ')]
explosive = {'Palm Fireworks': 0, 'Willow Fireworks': 0, 'Crossette Fireworks': 0}
successfully = False

while firework and power:
    current_firework = firework.popleft()
    current_power = power.pop()

    if current_firework <= 0:
        power.append(current_power)
        continue
    if current_power <= 0:
        firework.appendleft(current_firework)
        continue
    sums = current_firework + current_power

    if sums % 3 == 0 and sums % 5 != 0:
        explosive['Palm Fireworks'] += 1
    elif sums % 5 == 0 and sums % 3 != 0:
        explosive['Willow Fireworks'] += 1
    elif sums % 3 == 0 and sums % 5 == 0:
        explosive['Crossette Fireworks'] += 1
    else:
        current_firework -= 1
        firework.append(current_firework)
        power.append(current_power)

    if explosive['Palm Fireworks'] >= 3 and explosive['Willow Fireworks'] >= 3 and explosive['Crossette Fireworks'] >= 3:
        successfully = True
        break

if successfully:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if firework:
    print(f"Firework Effects left: {', '.join(str(x) for x in firework)}")
if power:
    print(f"Explosive Power left: {', '.join(str(x) for x in power)}")

print(f"Palm Fireworks: {explosive['Palm Fireworks']}")
print(f"Willow Fireworks: {explosive['Willow Fireworks']}")
print(f"Crossette Fireworks: {explosive['Crossette Fireworks']}")