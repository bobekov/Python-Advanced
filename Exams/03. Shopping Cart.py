def shopping_cart(*args):
    shopping = {'Pizza': [], 'Soup': [], 'Dessert': []}
    for command in args:
        meal = command[0]
        product = command[1]
        if command == 'Stop':
            break
        if meal == 'Pizza' and len(shopping['Pizza']) == 4:
            continue
        elif meal == 'Dessert' and len(shopping['Dessert']) == 2:
            continue
        elif meal == 'Soup' and len(shopping['Soup']) == 3:
            continue
        if product not in shopping[meal]:
            shopping[meal].append(product)

    for value in shopping.values():
        if len(value) > 0:
            break
    else:
        return "No products in the cart!"

    sorted_product = dict(sorted(shopping.items(), key=lambda x: (-len(x[1]), x[0])))
    result = ''
    for key, value in sorted_product.items():
        result += f"{key}:\n"
        sorted_product = sorted(value)
        for product in sorted_product:
            result += f" - {product}\n"

    return result