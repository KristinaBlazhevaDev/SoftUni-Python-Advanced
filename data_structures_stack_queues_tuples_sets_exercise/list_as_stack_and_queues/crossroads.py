from collections import deque

green_light = int(input())
free_window = int(input())

cars = deque()
passed_cars = 0
crashed = False

while True:
    command = input()
    if command == 'END':
        break

    if command != "green":
        cars.append(command)
    else:
        current_green = green_light

        while cars and current_green > 0:
            car = cars.popleft()

            if current_green >= len(car):
                current_green -= len(car)
                passed_cars += 1
            else:
                total_time = current_green + free_window

                if total_time >= len(car):
                    passed_cars += 1
                    current_green = 0
                else:
                    hit_car = car[total_time]
                    print("A crash happened!")
                    print(f"{car} was hit at {hit_car}.")
                    crashed = True
                    break
    if crashed:
        break
if not crashed:
    print("Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")
