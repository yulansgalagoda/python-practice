# daemon thread = a thread that runs in the background, not important for program to run
# the program won't wait for daemon threads to complete before exiting
# non-daemon threads cannot normally be killed
# common daemon threads are: background tasks, garbage collection, waiting for input, long-running processes

import threading
import time


def timer():
    print()
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for " + str(count) + " seconds")


timer_thread = threading.Thread(target=timer, args=(), daemon=True)
# timer_thread.setDaemon(True)          can only be used before a thread starts
timer_thread.start()

print(timer_thread.daemon)      # display whether a thread is daemon or not

answer = input("Do you want to exit?: ")
print()
