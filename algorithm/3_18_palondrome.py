from myds import Dqueue

def palcheck(aSring):
    chardeque = Dqueue()
    
    for ch in aSring:
        chardeque.addRear(ch)
        
    stillEqual = True
    
    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        # print(first, last)
        if first != last:
            stillEqual = False
            # print('not equal')
            
    return stillEqual
        
print(palcheck('asdfghgfdsa'))
print(palcheck('ghjhfg'))
