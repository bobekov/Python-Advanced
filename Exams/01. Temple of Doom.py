from collections import deque

tools = deque([int(x) for x in input().split()])
substances = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]

while tools and substances:
    first_element = tools.popleft()
    second_element = substances.pop()
    multiply = first_element * second_element

    if multiply in challenges:
        index = challenges.index(multiply)
        challenges.pop(index)
    else:
        first_element += 1
        tools.append(first_element)
        second_element -= 1
        substances.append(second_element)
        if second_element == 0:
            substances.pop()

if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")
else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print(f"Tools: {', '.join(str(x) for x in tools)}")
if substances:
    print(f"Substances: {', '.join(str(x) for x in substances)}")
if tools:
    print(f"Challenges: {', '.join(str(x) for x in challenges)}")



