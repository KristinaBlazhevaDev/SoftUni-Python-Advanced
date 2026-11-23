from collections import deque

robots_input = input().split(";")
robots = {}

for item in robots_input:
    robots_parts = item.split("-")
    name = robots_parts[0]
    process_tima = int(robots_parts[1])
    robots[name] = [process_tima, 0]

time_parts = input().split(":")
hours = int(time_parts[0])
minutes = int(time_parts[1])
seconds = int(time_parts[2])

total_seconds = hours * 3600 + minutes * 60 + seconds
products = deque()
while True:
    product = input()
    if product == "End":
        break
    products.append(product)

while products:
    total_seconds += 1
    current_product = products.popleft()
    is_taken = False

    for name, info in robots.items():
        process_tima = info[0]
        free_at = info[1]

        if total_seconds >= free_at:
            robots[name][1] = total_seconds + process_tima
            is_taken = True

            h = (total_seconds // 3600) % 24
            m = (total_seconds % 3600) // 60
            s = total_seconds % 60
            print(f"{name} - {current_product} [{h:02d}:{m:02d}:{s:02d}]")
            break

    if not is_taken:
        products.append(current_product)