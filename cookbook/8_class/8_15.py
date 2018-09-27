class Proxy():
    def __init__(self, obj):
        self._obj = obj

    # delegate attribute lookup to internal obj
    def __getattr__(self, item):
        print('getattr', item)
        return getattr(self._obj, item)

class Spam():
    def __init__(self, x):
        self.x = x

    def bar(self, y):
        print('Spam.bar:', self.x, y)



# 以下为补充1


class Fjs(object):
    def __init__(self, name):
        self.name = name

    def hello(self):
        print
        "said by : ", self.name

    def __getattribute__(self, item):
        print
        "访问了特性：" + item
        return object.__getattribute__(self, item)

# 以下为补充2


