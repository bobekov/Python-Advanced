from collections import deque

first = deque(input().split())
second = input().split()

flowers = ['rose', 'tulip', 'lotus', 'daffodil']
find_word = False
index_found = ''

while first and second:
    curr_one = first.popleft()
    curr_two = second.pop()

    for word in range(len(flowers)):
        if curr_one in flowers[word]:
            flowers[word] = flowers[word].replace(curr_one, '')
            if flowers[word] == '':
                find_word = True
                index_found = word
                break
        if curr_two in flowers[word]:
            flowers[word] = flowers[word].replace(curr_two, '')
            if flowers[word] == '':
                find_word = True
                index_found = word
                break

    if find_word:
        break

if not find_word:
    print("Cannot find any word!")
else:
    if index_found == 0:
        print("Word found: rose")
    elif index_found == 1:
        print("Word found: tulip")
    elif index_found == 2:
        print("Word found: lotus")
    elif index_found == 3:
        print("Word found: daffodil")

if first:
    print(f"Vowels left: {' '.join(first)}")
if second:
    print(f"Consonants left: {' '.join(second)}")
