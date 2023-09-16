# multiprocessing is running tasks in parallel on different CPU cores
# bypasses GIL used for threading
# multiprocessing is better for CPU bond tasks (heavy CPU usage)
# multithreading is better for IO bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():

    print(cpu_count())      # return the number of CPU cores in the PC

    a = Process(target=counter, args=(250000000,))
    b = Process(target=counter, args=(250000000,))
    c = Process(target=counter, args=(250000000,))
    d = Process(target=counter, args=(250000000,))

    start_time = time.perf_counter()

    a.start()
    b.start()
    c.start()
    d.start()

    a.join()
    b.join()
    c.join()
    d.join()

    end_time = time.perf_counter()

    print("finished in: ", end_time-start_time, "seconds")


if __name__ == "__main__":
    main()
