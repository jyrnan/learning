 import threading
import time

# worker thread
def worker(n, sema):
    # wait to be signaled
    sema.acquire()
    
    # do some work
    print('Working', n)
    
# creat some threads
sema =threading.Semaphore(0)
nworkers = 10
for n in range(nworkers):
    t = threading.Thread(target=worker, args=(n, sema,))
    t.start()
