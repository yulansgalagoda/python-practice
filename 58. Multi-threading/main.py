# thread = a flow of execution. like a separate order of instructions.
# Threads have to take turns when processing to achieve concurrency because of GIL.
# GIL = (global interpreter lock) is a feature which makes it run one thread at a time
# GIL allows one thread to hold the control of the interpreter at any given time
# therefore threads run concurrently but not parallel

# programs/tasks are two types as CPU bound and IO bound

# cpu bound = program/task spends most of its time waiting for internal events (CPU intensive)
# better to use multiprocessing (run threads parallel) with CPU bound programs

# IO bound = spends most of the time waiting for external events (user inputs, web scraping)
# better to use multithreading (run threads concurrently)

import threading
import time


def eat_breakfast():
    time.sleep(3)
    print("You ate breakfast")


def drink_coffee():
    time.sleep(4)
    print("You drank coffee")


def study():
    time.sleep(5)
    print("You studied")


x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join()    # thread synchronization: thread x should be done now before the main thread can move on
y.join()
z.join()

# eat_breakfast()
# drink_coffee()
# study()

print(threading.active_count())     # display number of threads running
print(threading.enumerate())        # display a list of all threads running
print(time.perf_counter())          # display time took by a thread
