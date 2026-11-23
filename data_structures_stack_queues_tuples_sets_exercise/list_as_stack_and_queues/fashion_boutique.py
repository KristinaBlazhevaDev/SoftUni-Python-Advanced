
clothes = ([int(x) for x in input().split()])
rack_capacity = int(input())

rack_count = 1
current_sum = 0
while clothes:
    current_cloth = clothes.pop()
    if current_sum + current_cloth <= rack_capacity:
        current_sum += current_cloth
    else:
        rack_count += 1
        current_sum = current_cloth
print(rack_count)
