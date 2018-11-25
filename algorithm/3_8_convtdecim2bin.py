from myds import Stack

def devideby2(decnum):
    remstack = Stack()

    while decnum > 0:
        rem = decnum % 2
        remstack.push(rem)
        decnum = decnum // 2

    binstr = ''
    while not remstack.isEmpty():
        binstr = binstr + str(remstack.pop())

    return binstr

def baseConverter(decnum, base=2):
    remstack = Stack()
    digits = '0123456789ABCDEF'

    while decnum > 0:
        rem = decnum % base
        remstack.push(rem)
        decnum = decnum // base

    newstring = ''
    while not remstack.isEmpty():
        newstring = newstring + digits[remstack.pop()]

    return newstring

print(devideby2(1025))
print(baseConverter(25,2))
print(baseConverter(29,16))
