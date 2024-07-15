from collections import deque

pizza_order = deque([int(x) for x in input().split(', ')])
employees = [int(x) for x in input().split(', ')]

total_pizza = 0
while pizza_order and employees:
    current_pizza_order = pizza_order.popleft()
    current_employees = employees.pop()

    if current_pizza_order <= 0:
        employees.append(current_employees)
    elif current_pizza_order > 10:
        employees.append(current_employees)
    elif current_pizza_order <= current_employees:
        total_pizza += current_pizza_order
    elif current_pizza_order > current_employees:
        total_pizza += current_employees
        current_pizza_order -= current_employees
        pizza_order.appendleft(current_pizza_order)

if not pizza_order:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizza}")
    print(f"Employees: {', '.join(str(x) for x in employees)}")
if not employees:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in pizza_order)}")


