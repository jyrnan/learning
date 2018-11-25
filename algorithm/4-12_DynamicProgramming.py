def recMC(coinValueList, change):
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change-i)
            if numCoins <= minCoins:
                minCoins = numCoins
        return minCoins


def recMC2(coinValueList, change, times=0):
    minCoins = change
    if change in coinValueList:
        times += 1
        return 1, times
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins, times = recMC2(coinValueList, change-i, times)
            numCoins = numCoins + 1
            times = times + 1
            if numCoins <= minCoins:
                minCoins = numCoins

        return minCoins, times

def recDC(coinValueList, change, knowResults={}):
    minCoins = change
    if change in coinValueList:
        knowResults[str(change)] = 1
        return 1
    elif str(change) in knowResults:
        return knowResults[str(change)]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recDC(coinValueList, change-i, knowResults)
            if numCoins <= minCoins:
                minCoins = numCoins
                knowResults[str(change)] = minCoins
        return minCoins


print(recDC([1, 5, 10, 25], 65))
