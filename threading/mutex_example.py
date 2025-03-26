import threading 
import time

class SharedCounter:
    def __init__(self):
        self.count = 0 
        self.mutex = threading.Lock()
        
    def increment(self):
        #Only one thread can execute this at a time
        with self.mutex:
            current = self.count
            time.sleep(0.5)
            self.count = current + 1
    
    def get_count(self):
        return self.count

def worker(counter, num_increments):
    for _ in range(num_increments):
        counter.increment()

counter = SharedCounter()

thread1 = threading.Thread(target=worker, args=(counter, 5))
thread2 = threading.Thread(target=worker, args=(counter, 5))

print("Starting threads...")
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()

print(f"Final count: {counter.get_count()}")
# Without the mutex, the final count would likely be less than 10 due to race conditions
# With the mutex, it will always be 10