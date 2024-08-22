import os, time
from multiprocessing import Process, current_process
from threading import Thread, current_thread


class TaskManager:

    def __init__(self, count, sleep):
        self.count = count
        self.sleep = sleep

    def io_bound(self):
        thread_name = current_thread().name
        process_name = current_process().name
        pid = os.getpid()

        print(f"{pid} * {process_name} * {thread_name} Sleep started.....")
        time.sleep(self.sleep)
        print(f"{pid} * {process_name} * {thread_name} Sleep completed.....")

    def cpu_bound(self):
        thread_name = current_thread().name
        process_name = current_process().name
        pid = os.getpid()
        
        print(f"{pid} * {process_name} * {thread_name} Count started.....")

        while self.count > 0:
            self.count -= 1
        
        print(f"{pid} * {process_name} * {thread_name} Count completed.....")


if __name__ == "__main__":
    tm = TaskManager(99999999, 10)
    start = time.time()
    tm.cpu_bound()
    tm.cpu_bound()
    end = time.time()
    print('time taken', end - start)

    start = time.time()
    p1 = Process(target = tm.cpu_bound)
    p2 = Thread(target = tm.cpu_bound)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.time()
    print('time taken', end - start)





