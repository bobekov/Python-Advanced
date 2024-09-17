from collections import deque

male = [int(x) for x in input().split()]
female = deque([int(x) for x in input().split()])

matches = 0
while male and female:
    current_male = male.pop()
    current_female = female.popleft()

    if current_male <= 0:
        female.appendleft(current_female)
    elif current_female <= 0:
        male.append(current_male)
    elif current_male % 25 == 0:
        if male:
            male.pop()
    elif current_female % 25 == 0:
        if female:
            female.popleft()
    elif current_male == current_female:
        matches += 1
    else:
        current_male -= 2
        male.append(current_male)

print(f"Matches: {matches}")
if not male:
    print("Males left: none")
else:
    print(f"Males left: {', '.join(str(x) for x in reversed(male))}")
if not female:
    print("Females left: none")
else:
    print(f"Females left: {', '.join(str(x) for x in female)}")
