from threading import Thread, Event
import time

# code to excute in an independent thread
def countdown(n, started_evt):
    print('countdown starting')
    started_evt.set()
    while n > 0:
        print('T_minus ', n)
        n -= 1
        time.sleep(5)
        
# creat the event object that will be used to signal startup
started_evt = Event()

# launch the thread and pass the start event 
t = Thread(target=countdown, args=(10, started_evt))
t.start()

# wait for the thread to start
started_evt.wait()
print('countdown is running')
