# stack = []
#
# n = int(input())
#
# for _ in range(n):
#     command, *data = input().split()
#
#     if command == "1":
#         stack.append(int(data.pop()))
#     elif command == "2":
#         if stack:
#             stack.pop()
#     elif command == "3":
#         if stack:
#             print(max(stack))
#     elif command == "4":
#         if stack:
#             print(min(stack))
#
# reversed_stack = []
# while stack:
#     reversed_stack.append(str(stack.pop()))
# print(", ".join(reversed_stack))

# ------------------------------------------------------------------------------------------

stack = []
n = int(input())

for _ in range(n):
    query = input().split()
    command = query[ 0 ]

    if command == "1":
        number = int(query[ 1 ])
        stack.append(number)
    elif command == "2":
        if stack:
            stack.pop()
    elif command == "3":
        if stack:
            print(max(stack))
    elif command == "4":
        if stack:
            print(min(stack))

reversed_stack = []
while stack:
    reversed_stack.append(str(stack.pop()))

print(", ".join(reversed_stack))

