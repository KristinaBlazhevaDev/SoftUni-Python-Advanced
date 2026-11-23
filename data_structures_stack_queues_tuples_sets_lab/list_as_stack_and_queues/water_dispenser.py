from collections import deque

water_quantity = int(input())
people = deque()

while True:
    name = input()
    if name == 'Start':
        break
    people.append(name)

while True:
    command = input()
    if command == 'End':
        break

    if command.startswith('refill'):
        litters_to_add = int(command.split()[1])
        water_quantity += litters_to_add
    else:
        litters_wanted = int(command)
        person = people.popleft()

        if water_quantity >= litters_wanted:
            water_quantity -= litters_wanted
            print(f"{person} got water")
        else:
            print(f"{person} must wait")

print(f"{water_quantity} liters left")