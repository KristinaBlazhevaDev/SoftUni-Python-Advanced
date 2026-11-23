from collections import deque
n = int(input())
pumps = deque()

for index in range(n):
    petrol, distance = [int(x) for x in input().split()]
    pumps.append([petrol, distance, index])

while True:
    tank = 0
    stops = 0
    for pump in pumps:
        petrol = pump[0]
        distance = pump[1]
        tank += petrol
        if tank >= distance:
            tank -= distance
            stops += 1
        else:
            break
    if stops == n:
        print(pumps[0][2])
        break
    else:
        pumps.append(pumps.popleft())
