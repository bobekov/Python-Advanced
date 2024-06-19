from collections import deque

size_eggs = deque([int(x) for x in input().split(', ')])
paper = deque([int(x) for x in input().split(', ')])

box = 0
while size_eggs and paper:
    wrap_egg = size_eggs[0] + paper[-1]

    if size_eggs[0] <= 0:
        size_eggs.popleft()
    elif size_eggs[0] == 13:
        size_eggs.popleft()
        paper[0], paper[-1] = paper[-1], paper[0]
    elif wrap_egg <= 50:
        size_eggs.popleft()
        paper.pop()
        box += 1
    else:
        size_eggs.popleft()
        paper.pop()

if box > 0:
    print(f"Great! You filled {box} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if size_eggs:
    print(f"Eggs left: {', '.join(str(x) for x in size_eggs)}")
if paper:
    print(f"Pieces of paper left: {', '.join(str(x) for x in paper)}")