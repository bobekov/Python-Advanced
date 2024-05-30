def shop_from_grocery_list(budget, grocery_list, *args):
    purchase_product = []
    for product, price in args:
        if product not in grocery_list:
            continue
        if budget - float(price) < 0:
            break
        else:
            purchase_product.append(product)
            grocery_list.remove(product)
            budget -= float(price)

    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."