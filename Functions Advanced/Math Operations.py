def math_operations(*args, **kwargs):
    for i in range(len(args)):
        if i % 4 == 0:
            kwargs['a'] += args[i]
        elif i % 4 == 1:
            kwargs['s'] -= args[i]
        elif i % 4 == 2:
            if not args[i] == 0:
                kwargs['d'] /= args[i]
        else:
            kwargs['m'] *= args[i]

    result = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    # for key, value in result:
    #     print(f'{key}: {value}')

    return '\n'.join([f'{key}: {value:.1f}' for key, value in result])