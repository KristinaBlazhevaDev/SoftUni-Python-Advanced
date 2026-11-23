from collections import deque

kids = deque(input().split())
count = int(input())

while len(kids) > 1:
    for _ in range(count -1):
        kid = kids.popleft()    # съкратено : kids.append(kids.popleft())
        kids.append(kid)

    removed_kid = kids.popleft()
    print(f"Removed {removed_kid}")

print(f"Last is {kids.popleft()}")