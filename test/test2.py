from datetime import datetime
import sched
import time
import threading

def timeTask(n):
    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(n, 1, task, (n,))
    scheduler.run()

def task(n):
    print(('threading %d....' % n) + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=task(i))
        t.start()
        t.join()
    print('Game Over')