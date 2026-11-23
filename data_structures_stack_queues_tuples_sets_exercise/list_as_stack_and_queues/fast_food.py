from collections import deque

food_quantity = int(input())

orders = deque([int(x) for x in input().split()])

print(max(orders))

while orders:
    current_order = orders[0]

    if food_quantity >= current_order:
        food_quantity -= orders.popleft()
    else:
        break

if not orders:
    print("Orders complete")
else:
    left_orders = " ".join([str(x) for x in orders])
    print(f"Orders left: {left_orders}")

