# import threading
# import time

# class SharedResourceThread(threading.Thread):
#     # Class variable that will be shared among all instances of the class
#     counter = 0
    
    
#     def __init__(self, name):
#         threading.Thread.__init__(self)
#         self.name = name
    
#     def run(self):
#         lock = threading.Lock()
#         # Each thread will try to increment the counter 100,000 times
#         for _ in range(100000):
#             # Simulate some work with a tiny sleep to increase the chance of context switching
#             lock.acquire()
#             step = 1
#             time.sleep(0.00001)
#             temp_res = SharedResourceThread.counter + step
#             time.sleep(0.00001)
#             SharedResourceThread.counter = temp_res
#             lock.release()


# # Create two threads
# thread1 = SharedResourceThread("Thread-1")
# thread2 = SharedResourceThread("Thread-2")

# # Start both threads
# thread1.start()
# thread2.start()

# # Wait for both threads to complete
# thread1.join()
# thread2.join()

# # The final value of the counter should be 200,000 (100,000 increments per thread)
# print("Final counter value:", SharedResourceThread.counter)

# The lock will not work for the above code
# Why the Lock Doesn't Work:
# Separate Locks: Since the lock is created within the run method, each thread creates its own lock object. This means that when thread1 acquires its lock, thread2 is not blocked from accessing the counter because it has its own independent lock.
# No Synchronization: For the Lock to properly synchronize access to the shared resource, both threads need to share the same Lock object. Otherwise, the locking mechanism is ineffective, and race conditions can occur.

import threading
import time

class SharedResourceThread(threading.Thread):
    # Class variable that will be shared among all instances of the class
    counter = 0
    lock = threading.Lock()  # Create a single lock for all threads

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    
    def run(self):
        # Each thread will try to increment the counter 100,000 times
        for _ in range(100000):
            # Simulate some work with a tiny sleep to increase the chance of context switching
            # with SharedResourceThread.lock:  # Use a single lock shared by all threads
            #     step = 1
            #     time.sleep(0.00001)
            #     temp_res = SharedResourceThread.counter + step
            #     time.sleep(0.00001)
            #     SharedResourceThread.counter = temp_res
            
            # lock without using 'with'
            SharedResourceThread.lock.acquire()
            step = 1
            time.sleep(0.00001)
            temp_res = SharedResourceThread.counter + step
            time.sleep(0.00001)
            SharedResourceThread.counter = temp_res
            SharedResourceThread.lock.release()


# Create two threads
thread1 = SharedResourceThread("Thread-1")
thread2 = SharedResourceThread("Thread-2")

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()

# The final value of the counter should be 200,000 (100,000 increments per thread)
print("Final counter value:", SharedResourceThread.counter)

# Since 2 threads share same lock object here locking will work properly