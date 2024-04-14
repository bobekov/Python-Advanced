text = tuple(input())

unique = sorted(set(text))

for el in unique:
    print(f'{el}: {text.count(el)} time/s')