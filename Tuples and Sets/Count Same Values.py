numbers = tuple(float(x) for x in input().split())

occurrence = {}

for num in numbers:
    if num not in occurrence:
        occurrence[num] = numbers.count(num)
        print(f"{num} - {numbers.count(num)} times")