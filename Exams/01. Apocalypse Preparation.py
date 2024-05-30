from collections import deque

textiles = deque([int(x) for x in input().split()])
medicaments = [int(x) for x in input().split()]

items = {"Patch": 0, "Bandage": 0, "MedKit": 0}

while textiles and medicaments:
    curr_textile = textiles.popleft()
    curr_medicament = medicaments.pop()
    sum_item = curr_textile + curr_medicament

    if sum_item == 30:
        items['Patch'] += 1
    elif sum_item == 40:
        items["Bandage"] += 1
    elif sum_item == 100:
        items["MedKit"] += 1
    elif sum_item > 100:
        items["MedKit"] += 1
        sum_item -= 100
        medicaments[-1] += sum_item
    else:
        curr_medicament += 10
        medicaments.append(curr_medicament)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

sort_items = sorted(items.items(), key=lambda x: (-x[1], x[0]))
for item in sort_items:
    if int(item[1]) > 0:
        print(f"{item[0]} - {item[1]}")

if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join(str(x) for x in medicaments)}")
if textiles:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")







