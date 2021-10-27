import cv2
import time
import keyboard
import random
from utils.grabscreen import grab_screen

# File for stats
f = open("stats.csv", "w")


time.sleep(5)
keyboard.press('space')
keyboard.release("space")

program_time = time.time()
episode_scores = []

# Enter number of episodes you want to run.
for i in range(5000):

    # Choose look ahead amount at random
    start_ahead = random.randint(80, 120)
    ahead = start_ahead

    # Choose amount of time before increasing look ahead.
    start_speedup = random.randint(190, 210)
    count = 0

    # Setting zero and white we will flip when game colors invert
    zero = 0
    white = 255

    # Starts game
    keyboard.press('space')
    time.sleep(2)
    keyboard.release("space")
    episode_start = time.time()
    start = time.time()

    # Bot rules you must update pixels!
    while True:
        last_time = time.time()
        image = grab_screen(region=(85, 350, 715, 500))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        (thresh, image) = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

        if image[144][376] == zero:
            ahead += 4
            holder = zero
            zero = white
            white = holder

        # Three cactus small
        if image[92][ahead] == zero or image[92][ahead - 1] == zero or image[92][ahead - 2] == zero:
            keyboard.release("down")
            keyboard.press("space")
            time.sleep(0.01)
            keyboard.release("space")

        # DUCK
        elif image[54][ahead] == zero:
            #print("down")
            keyboard.press("down")

        # White background end test
        if image[45][395] == white and image[35][370] == zero and image[35][420] == zero:
            keyboard.release("space")
            keyboard.release("down")
            break

        count += int(time.time() - start)

        if count > start_speedup:
            count = 0
            start = time.time()
            ahead += 1
            #print(ahead)

    episode_score = int(time.time() - episode_start)
    if len(episode_scores) > 0:
        if max(episode_scores) < episode_score:
            print(f"New Max Score: {episode_score}\nEpisode: {i}\nTime: {int(time.time() - program_time)}")
            print(f"Look Ahead {ahead}")
    
    f.write(f"{i},{episode_score},{start_ahead},{start_speedup}\n")
    print(f"{i},{episode_score},{start_ahead},{start_speedup}\n")
    episode_scores.append(episode_score)
    keyboard.press('space')
    time.sleep(2)
    keyboard.release("space")

print(f"Episodes: {len(episode_scores)}")
print(f"Max: {max(episode_scores)}")
print(f"Average: {sum(episode_scores) / len(episode_scores)}")
f.close()