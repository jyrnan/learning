from stack import Stack

def parchecker(symbolstring):
    s = Stack()
    balenced = True
    index = 0
    while index < len(symbolstring) and balenced:
        symbol = symbolstring[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balenced == False
                break
            else:
                s.pop()

        index += 1

    if balenced and s.isEmpty():
        return True
    else:
        return False


print(parchecker('((()))'))
print(parchecker('(()'))