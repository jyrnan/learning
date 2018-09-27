class A():
    cat = 'cat'

    def spam(self, x):
        print('A.spam', x)

    def foo(self):
        print('A.foo')

    def __getattr__(self, item):
        return item


class B():
    def __init__(self):
        self._a = A()

    def spma(self, x):
        print('B.spam', x)
        self._a.spam(x)

    def bar(self):
        print('B.bar')

    def __getattr__(self, item):
        return getattr(self._a, item)