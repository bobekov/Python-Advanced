def list_manipulator(list_num, first, second, *args):
    if first == 'add' and second == 'beginning':
        list_num = list(args) + list_num

    elif first == 'add' and second == 'end':
        list_num.extend(args)

    elif first == 'remove' and second == 'beginning':
        if args:
            number = args[0]
            list_num = list_num[number:]
        else:
            list_num = list_num[1:]
    elif first == 'remove' and second == 'end':
        if args:
            number = args[0]
            list_num = list_num[:number-1]
        else:
            list_num = list_num[:-1]

    return list_num