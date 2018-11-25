def tostr(n, base):
    convertString = '0123456789ABCDEF'
    if n < base:
        return convertString[n]
    else:
        return tostr(n//base, base) + convertString[n%base]

print(tostr(10, 2))

def reverseStr(string):
    if len(string) == 1:
        return string
    else:
        return reverseStr(string[1:]) + string[0]


print(reverseStr('apple'))

def palindromaCheck(string):
    string = string.replace(' ','').lower()
    return string == reverseStr(string)


print(palindromaCheck('ai bohphoBia'))