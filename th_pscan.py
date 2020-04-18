import threading
from queue import Queue
import time
import socket

# threaded scan open ports on a server/ website

# a print_lock is what is used to prevent "double" modification of shared variables.
# this is used so while one thread is using a variable, others cannot access
# it. Once done, the thread releases the print_lock.
# to use it, you want to specify a print_lock per thing you wish to print_lock.
ports=[]
def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target, port))
        with print_lock:
            print('port', port)
            ports.append(port)
        con.close()
    except:
        pass

def threader():
    '''Pulls an worker from the queue and processes it'''
    while True:
        # gets an worker from the queue
        worker = q.get()

        # Run the example job with the avail worker in queue (thread)
        portscan(worker)

        # completed with the job
        q.task_done()


if __name__ == '__main__':
    print_lock = threading.Lock()
    target = 'localhost'
    # Create the queue and threader
    q = Queue()
    # how many threads are we going to allow for
    for x in range(400):
        t = threading.Thread(target=threader)
        # classifying as a daemon, so they will die when the main dies
        t.daemon = True
        # begins, must come after daemon definition
        t.start()

    start = time.time()
    # 100 jobs assigned.
    for worker in range(1, 8001):
        q.put(worker)
    # wait until the thread terminates.
    q.join()
    print(f'Ports open: {ports}')
