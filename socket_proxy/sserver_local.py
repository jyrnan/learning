from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
from urllib.parse import urlparse
import argparse

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        url = self.path
        result = urlparse(url)
        # print(url, '\n')
        # print(self.headers, '\n')
        # print(result.netloc)
        # print(type(self.headers))
    
        path = result.path
        if ':' in result.netloc:
            host, port = result.netloc.split(':')
        else:
           host, port = result.netloc, '80'
        #print(host, port)
        port = int(port)
        host_ip = socket.gethostbyname(host)
        

        del self.headers['Proxy-Connection']
        self.headers['Connection'] = 'close' 

        send_data = 'GET ' + path + ' ' + self.protocol_version + '\r\n'
        head = ''
        for key, val in self.headers.items():
            head = head + "%s: %s\r\n" % (key, val)
        send_data = send_data + head + '\r\n'
        print(send_data)

        so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #so.connect((host_ip, port))
        so.connect(('127.0.0.1', 10000))
        so.sendall(url.encode('ascii'))
        so.shutdown(socket.SHUT_WR)

        data = b''
        while True:
            tmp = so.recv(4096)
            if not tmp:
                break
            data = data + tmp

        so.close()

        self.wfile.write(data)
    
    # def do_CONNECT(self):
    #     url = self.path
    #     result = urlparse(url)
    #     # print(url, '\n')
    #     # print(self.headers, '\n')
    #     # print(result.netloc)
    #     # print(type(self.headers))
    
    #     path = result.path
    #     if ':' in result.netloc:
    #         host, port = result.netloc.split(':')
    #     else:
    #        host, port = result.netloc, '80'
    #     #print(host, port)
    #     port = int(port)
    #     host_ip = socket.gethostbyname(host)
        

    #     del self.headers['Proxy-Connection']
    #     self.headers['Connection'] = 'close' 

    #     send_data = 'GET ' + path + ' ' + self.protocol_version + '\r\n'
    #     head = ''
    #     for key, val in self.headers.items():
    #         head = head + "%s: %s\r\n" % (key, val)
    #     send_data = send_data + head + '\r\n'
    #     print(send_data)

    #     so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     #so.connect((host_ip, port))
    #     so.connect(('127.0.0.1', 10000))
    #     so.sendall(url.encode('ascii'))
    #     so.shutdown(socket.SHUT_WR)

    #     data = b''
    #     while True:
    #         tmp = so.recv(4096)
    #         if not tmp:
    #             break
    #         data = data + tmp

    #     so.close()

    #     self.wfile.write(data)
    

def main(port=8080):
    try:
        server = HTTPServer(('', port), MyHandler)
        print('Welcom...')
        server.serve_forever()
    except KeyboardInterrupt:
        print('Teminated...')
        server.socket.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Send and recive UDP,' 'pretending packet are often dropped')
    parser.add_argument('-p', metavar='PORT', type=int, default=8080, help='UDP port(default 8080)')
    args = parser.parse_args()
    main(args.p)