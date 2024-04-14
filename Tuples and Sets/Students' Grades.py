numbers = int(input())
occ = {}

for _ in range(numbers):
    name, grade = input().split()
    if name not in occ:
        occ[name] = [float(grade)]
    else:
        occ[name].append(float(grade))

for key, value in occ.items():
    grades = [f'{x:.2f}' for x in value]
    print(f"{key} -> {' '.join(grades)} (avg: {sum(value) / len(value):.2f})")