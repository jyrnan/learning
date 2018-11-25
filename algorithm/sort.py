def buble_sort(a):
    b = list(a)
    m = len(b)
    while (m-1):
        for n in range(m-1):
            if b[n] > b[n+1]:
                b[n], b[n+1] = b[n+1], b[n]
        m -= 1
    return b


def buble_sort2(a):
    minus = []
    if len(a) == 1:
        return a
    else:
        minus.append(min(a))
        print(minus)
        a.remove(min(a))
    return minus + buble_sort2(a)
    
def quick_sort(a):
    lenth = len(a)
    if lenth == 1:
        return a
    if lenth == 2 and a[0] <= a[1]:
        return a
    else:
        a[0], a[1] = a[1], a[0]
        return a
        
    l = 1
    r = lenth
    while :
        while  True:
            if a[r] > a[0]:
                r -= 1
            else: break
        while a[l] < a[0]:
            l
    
a = [3, 7, 4, 8]
print(buble_sort2(a))
