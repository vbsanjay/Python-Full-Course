import os, time
from threading import Thread, current_thread
from multiprocessing import Process, current_process


SECOND = 10
COUNT = 10000000

def io_bound(sec):
    pid = os.getpid()
    thread_name = current_thread().name
    process_name = current_process().name

    print(f"pid: {pid}, thread_name: {thread_name}, process_name: {process_name}, started sleeping..... ")
    time.sleep(sec)
    print(f"pid: {pid}, thread_name: {thread_name}, process_name: {process_name}, stoped sleeping..... ")


def cpu_bound(n):
    pid = os.getpid()
    thread_name = current_thread().name
    process_name = current_process().name

    print(f"pid: {pid}, thread_name: {thread_name}, process_name: {process_name}, started counting..... ")
    count = 1
    while count != n:
        if count % 100000 == 0:
            print("milestone passed on", thread_name)
        count += 1


    print(f"pid: {pid}, thread_name: {thread_name}, process_name: {process_name}, stoped counting..... ")


if __name__ == "__main__":
    start = time.time()

    # io_bound(SECOND)
    # io_bound(SECOND)
    cpu_bound(COUNT)
    cpu_bound(COUNT)
    # t1 = Thread(target = io_bound, args=[SECOND])
    # t2 = Thread(target = io_bound, args=[SECOND])
    # t1 = Thread(target = cpu_bound, args=[COUNT])
    # t2 = Thread(target = cpu_bound, args=[COUNT])
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()

    end = time.time()

    print("program done executing. time taken in seconds = ", end - start)