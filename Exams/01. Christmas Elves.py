from collections import deque

elf_energy = deque([int(x) for x in input().split()])
material_box = deque([int(x) for x in input().split()])

toys = 0
energy = 0
moves = 1
while elf_energy and material_box:
    current_elf = elf_energy.popleft()
    current_box = material_box.pop()

    if current_elf < 5:
        material_box.appendleft(current_box)
        moves += 1
        continue
    elif current_elf < current_box:
        material_box.appendleft(current_box)
        elf_energy.append(current_elf * 2)
    elif moves % 3 == 0:
        require_energy = current_box * 2
        if current_elf >= require_energy:
            current_elf -= require_energy
            elf_energy.append(current_elf + 1)
            toys += 2
            energy += require_energy
        else:
            elf_energy.append(current_elf * 2)
            material_box.appendleft(current_box)
    elif moves % 5 == 0:
        if current_elf >= current_box * 2:
            current_elf -= current_box
            elf_energy.append(current_elf)
            energy += current_box * 2
        elif current_elf >= current_box:
            current_elf -= current_box
            elf_energy.append(current_elf)
            energy += current_box
        else:
            elf_energy.append(current_elf)
            material_box.appendleft(current_box)
    elif current_elf >= current_box:
        current_elf -= current_box - 1
        elf_energy.append(current_elf)
        energy += current_box
        toys += 1
    moves += 1

print(f"Toys: {toys}")
print(f"Energy: {energy}")
if elf_energy:
    print(f"Elves left: {', '.join(str(x) for x in elf_energy)}")
if material_box:
    print(f"Boxes left: {', '.join(str(x) for x in material_box)}")
