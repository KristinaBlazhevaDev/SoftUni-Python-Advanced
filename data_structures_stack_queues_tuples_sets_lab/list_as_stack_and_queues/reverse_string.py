stack = list(input())

while stack:
    print(stack.pop(), end="")


# ----------------------------------------------------------------------------

text = list(input())
stack = []
for i in range(len(text)):
 stack.append(text.pop())
print("".join(stack))