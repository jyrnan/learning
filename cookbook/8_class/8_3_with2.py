#为了让一个对象兼容with语句， 你需要实现__enter__和__exit__()方法。

from socket import socket, AF_INET, SOCK_STREAM

class LazyConnections:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.connections = []

    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.connections.pop().close()

from functools import partial

conn = LazyConnections(('www.python.org', 80))
# Connection closed

with conn as s:
    # conn.__enter__() executes: connection open
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))
    # conn.__exit__() excutes: connection closed
    print(resp)
    with conn as s2:
        s2.send(b'GET /index.html HTTP/1.0\r\n')
        s2.send(b'Host: www.python.org\r\n')
        s2.send(b'\r\n')
        resp2 = b''.join(iter(partial(s2.recv, 8192), b''))
        print(resp2)
