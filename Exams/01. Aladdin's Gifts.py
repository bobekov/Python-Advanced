from collections import deque

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])
presents = {'Gemstone': 0, 'Porcelain Sculpture': 0, 'Gold': 0, 'Diamond Jewellery': 0}

while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()
    product = current_material + current_magic

    if product < 100:
        if product % 2 == 0:
            product = current_material * 2 + current_magic * 3
        else:
            product *= 2
    if product > 499:
        product /= 2
    if 100 <= product <= 199:
        presents['Gemstone'] += 1
    elif 200 <= product <= 299:
        presents['Porcelain Sculpture'] += 1
    elif 300 <= product <= 399:
        presents['Gold'] += 1
    elif 400 <= product <= 499:
        presents['Diamond Jewellery'] += 1

if presents['Gemstone'] > 0 and presents['Porcelain Sculpture'] > 0 \
        or presents['Gold'] > 0 and presents['Diamond Jewellery'] > 0:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

for name, num in presents.items():
    if num:
        print(f"{name}: {num}")

