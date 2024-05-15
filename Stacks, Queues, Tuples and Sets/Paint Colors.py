from collections import deque

colors_sting = deque(input().split())

main_color = ['red', 'blue', 'yellow']
secondary_colors = {'orange': ['red', 'yellow'],
                    'purple': ['red', 'blue'],
                    'green': ['blue', 'yellow']}

collected_colors = []

while colors_sting:
    first_str = colors_sting.popleft()
    last_str = colors_sting.pop() if colors_sting else ''
    if first_str + last_str in main_color or first_str + last_str in secondary_colors:
        collected_colors.append(first_str + last_str)
    elif last_str + first_str in main_color or last_str + first_str in secondary_colors:
        collected_colors.append(last_str + first_str)
    else:
        if len(first_str) > 1:
            colors_sting.insert(len(colors_sting) // 2, first_str[:-1])
        if len(last_str) > 1:
            colors_sting.insert(len(colors_sting) // 2, last_str[:-1])

for color in collected_colors:
    if color in secondary_colors:
        for el in secondary_colors[color]:
            if el not in collected_colors:
                collected_colors.remove(color)
                break

print(collected_colors)