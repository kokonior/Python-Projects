import time, random

print("Ready?")

time.sleep(random.randint(1, 5))

a = time.time()

input("ENTER NOW!")

x = time.time()

print(f"your time: {x-a}s")
