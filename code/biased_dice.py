import random
listt = [1,2,3,4,5,6,6]
no_of_times = int(input("How many times you want to roll the dice : "))
count = 0
while True:
    if count == no_of_times:
        print("Chances over")
        break
    ran_num = random.choice(listt)
    print(f"Game no {count+1} starts and the random number generated is {ran_num}")
    count += 1



