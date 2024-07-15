def flights(*args):
    planes = {}
    index = 0

    while index < len(args):
        destination = args[index]
        if destination == 'Finish':
            break
        passengers = args[index + 1]

        if destination not in planes:
            planes[destination] = 0
        planes[destination] += passengers

        index += 2

    return planes