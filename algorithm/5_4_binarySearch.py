def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True

        else:
            if item < alist[midpoint]:
                last = midpoint - 1

            else:
                first = midpoint + 1

    return found


def binarySearchRecur(alist, item):
    first = 0
    last = len(alist) -1
    midpoint = (first + last) // 2
    print (first, midpoint, last, alist[first],  alist[midpoint], alist[last])

    if last == 0:
        return alist[midpoint] == item
    elif alist[midpoint] == item:
        return True
    elif item < alist[midpoint]:
        return binarySearchRecur(alist[:midpoint], item)
    else:
        return binarySearchRecur(alist[midpoint+1:], item)

testlist = list(range(1000))

import random


def test():  # test module
    result = True
    for i in range(100):
        test = random.randrange(2000)
        print(test)
        result1 = binarySearchRecur(testlist, test)
        result2 = (test in testlist)
        print(result1, result2)
        if result1 != result2:
            result = False
            print('Something wrong')
            break

    print('result is ', result)

test()
