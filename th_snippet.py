import threading
from queue import Queue
import time

print_lock = threading.Lock()

# function here
def function(arg):
    time.sleep(2)

def threader():
    while True:
        worker = q.get()
        function(worker)
        q.task_done()

q = Queue()

# def ranges(length, other_length):
for x in range(30):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start

for worker in range(1,20):
    q.put(worker)

# ranges(10, 20)
q.join()