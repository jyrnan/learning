import threading, time


def job1():
    global A, t
    #t.acquire()
    for i in range(10):
        A += 1
        print('job1', A)
        time.sleep(1)
    #t.release()


def job2():
    global A, t
    #t.acquire()
    for i in range(10):
        A += 10
        print('job2', A)
    #t.release()


if __name__ == '__main__':
    A = 0
    t = threading.Lock()
    t1 = threading.Thread(target=job1())
    t2 = threading.Thread(target=job2())
    t1.start()
    t2.start()
    t1.join()
    t2.join()