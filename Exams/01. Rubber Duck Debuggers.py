from collections import deque

time_task = deque([int(x) for x in input().split()])
number_tasks = [int(x) for x in input().split()]

ducky_type = {'Darth Vader Ducky': 0, 'Thor Ducky': 0, 'Big Blue Rubber Ducky': 0, 'Small Yellow Rubber Ducky': 0}

while time_task and number_tasks:
    curr_time_task = time_task.popleft()
    curr_number_tasks = number_tasks.pop()
    multiply = curr_time_task * curr_number_tasks

    if 0 <= multiply <= 60:
        ducky_type['Darth Vader Ducky'] += 1
    elif 60 < multiply <= 120:
        ducky_type['Thor Ducky'] += 1
    elif 120 < multiply <= 180:
        ducky_type['Big Blue Rubber Ducky'] += 1
    elif 180 < multiply <= 240:
        ducky_type['Small Yellow Rubber Ducky'] += 1
    else:
        number_tasks.append(curr_number_tasks - 2)
        time_task.append(curr_time_task)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for key, value in ducky_type.items():
    print(f"{key}: {value}")