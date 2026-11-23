from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
intelligence_value = int(input())

bullets_fired = 0
barrel_shots = 0

first_idx = 0

while bullets and locks:
    current_bullet = bullets.pop()
    bullets_fired += 1
    barrel_shots += 1

    current_lock = locks[first_idx]
    if current_bullet <= current_lock:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")
        
    if barrel_shots == barrel_size and bullets:
        print("Reloading!")
        barrel_shots = 0

if not locks:
    money_earned = intelligence_value - (bullets_fired * bullet_price)
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")

