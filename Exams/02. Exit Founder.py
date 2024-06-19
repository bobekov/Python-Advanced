first, second = input().split(', ')
matrix = [[x for x in input().split()] for _ in range(6)]

first_player_rest = False
second_player_rest = False
while True:
    command = input()
    if not first_player_rest:
        row, col = int(command[1]), int(command[4])
        if matrix[row][col] == 'E':
            print(f"{first} found the Exit and wins the game!")
            break
        elif matrix[row][col] == 'T':
            print(f"{first} is out of the game! The winner is {second}.")
            break
        elif matrix[row][col] == 'W':
            print(f"{first} hits a wall and needs to rest.")
            first_player_rest = True
    else:
        first_player_rest = False

    command = input()
    if not second_player_rest:
        row, col = int(command[1]), int(command[4])
        if matrix[row][col] == 'E':
            print(f"{second} found the Exit and wins the game!")
            break
        elif matrix[row][col] == 'T':
            print(f"{second} is out of the game! The winner is {first}.")
            break
        elif matrix[row][col] == 'W':
            print(f"{second} hits a wall and needs to rest.")
            second_player_rest = True
    else:
        second_player_rest = False