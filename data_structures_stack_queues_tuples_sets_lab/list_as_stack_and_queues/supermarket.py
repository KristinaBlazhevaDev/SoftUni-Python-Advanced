from collections import deque

customers = deque()

while True:
    command = input()
    if command == 'End':
        break

    if command == 'Paid':
        while customers:
            print(customers.popleft())
    else:
        customers.append(command)
print(f"{len(customers)} people remaining.")

# -------------------------------------------------------------------------------

# from collections import deque
# queue = deque()
# while True:
#     command = input()
#     if command == "Paid":
#         while len(queue):
#             print(queue.popleft())
#     elif command == "End":
#         print(f"{len(queue)} people remaining.")
#         break
#     else:
#         queue.append(command)