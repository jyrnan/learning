import time

class Date:
    """使用类方法"""
    # primary constructor
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    #alternate constructor
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


a = Date(2012, 12, 21)
b = Date.today()