def bubbleSort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                exchanges = True
        passnum = passnum - 1

# test code
import time
import random


alist = list((random.randrange(100000) for i in range(5000)))
blist = alist[:]
start = time.time()
shortBubbleSort(alist)
mid = time.time()
blist.sort()
end = time.time()
last1 = mid -start
last2 = end - mid
print('timelast %4.5f , %4.5f seconds' % (last1, last2))
print(alist)
print(blist)

