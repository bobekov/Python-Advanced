def start_spring(**kwargs):
    type_spring = {}
    for key, value in kwargs.items():
        if value not in type_spring:
            type_spring[value] = []
        type_spring[value].append(key)

    sort_spring = sorted(type_spring.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ''
    for element in sort_spring:
        result += f"{element[0]}:\n"
        sort_collection = sorted(element[1])
        for el in sort_collection:
            result += f"-{el}\n"

    return result