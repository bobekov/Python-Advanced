def shopping_list(budget, **kwargs):
    products = {}
    for product, data in kwargs.items():
        price, quantity = float(data[0]), int(data[1])
        total_price = price * quantity
        if len(products) == 5:
            break
        if budget >= total_price:
            products[product] = total_price
            budget -= total_price
        if budget <= 1:
            return "You do not have enough budget."

    result = ''
    for key, value in products.items():
        result += f"You bought {key} for {value:.2f} leva.\n"

    return result