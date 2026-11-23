from collections import deque

cups = deque([int(i) for i in input().split()])
bottles = [int(i) for i in input().split()]
wasted_water = 0

while cups and bottles:
    current_cup = cups.popleft()
    current_bottle = bottles.pop()

    if current_bottle >= current_cup:
        wasted_water += current_bottle - current_cup
    else:
        current_cup -= current_bottle
        cups.appendleft(current_cup)
if not cups:
    remaining_cups = " ".join([str(i) for i in bottles[::-1]])
    print(f"Bottles: {remaining_cups}")
else:
    remaining_cups = " ".join([str(i) for i in cups])
    print(f"Cups: {remaining_cups}")
print(f"Wasted litters of water: {wasted_water}")

