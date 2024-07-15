def stock_availability(inventory, action, *params):
    if action == "delivery":
        inventory.extend(params)
    elif action == "sell":
        if not params:
            inventory.pop(0)
        else:
            for param in params:
                if isinstance(param, int):
                    for _ in range(param):
                        inventory.pop(0)
                else:
                    while param in inventory:
                        inventory.remove(param)
    return inventory