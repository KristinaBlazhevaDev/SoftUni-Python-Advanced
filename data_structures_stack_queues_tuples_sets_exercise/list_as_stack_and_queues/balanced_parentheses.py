sequence = input()
stack = []

pairs = {
    "(": ")",
    "[": "]",
    "{": "}"
}

is_balanced = True

for char in sequence:
    if char in '([{':
        stack.append(char)
    elif char in ")]}":
        if not stack:
            is_balanced = False
            break

        last_open = stack.pop()
        if pairs[last_open] != char:
            is_balanced = False
            break
if is_balanced and not stack:
    print("YES")
else:
    print("NO")