from collections import deque

effects = deque([int(x) for x in input().split(', ')])
casings = [int(x) for x in input().split(', ')]

bombs = {'Datura Bombs': 0, 'Cherry Bombs': 0, 'Smoke Decoy Bombs': 0}
while effects and casings:
    current_effects = effects.popleft()
    current_casings = casings.pop()
    sums = current_effects + current_casings

    if sums == 40:
        bombs['Datura Bombs'] += 1
    elif sums == 60:
        bombs['Cherry Bombs'] += 1
    elif sums == 120:
        bombs['Smoke Decoy Bombs'] += 1
    else:
        current_casings -= 5
        effects.appendleft(current_effects)
        casings.append(current_casings)

    if bombs['Datura Bombs'] >= 3 and bombs['Cherry Bombs'] >= 3 and bombs['Smoke Decoy Bombs'] >= 3:
        print("Bene! You have successfully filled the bomb pouch!")
        break

if bombs['Datura Bombs'] < 3 or bombs['Cherry Bombs'] < 3 or bombs['Smoke Decoy Bombs'] < 3:
    print("You don't have enough materials to fill the bomb pouch.")
if not effects:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join(str(x) for x in effects)}")
if not casings:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join(str(x) for x in casings)}")

print(f"Cherry Bombs: {bombs['Cherry Bombs']}")
print(f"Datura Bombs: {bombs['Datura Bombs']}")
print(f"Smoke Decoy Bombs: {bombs['Smoke Decoy Bombs']}")
