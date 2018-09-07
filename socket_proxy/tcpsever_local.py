from socketserver import BaseRequestHandler, TCPServer
import argparse
import requests

class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        while True:
            msg = self.request.recv(8192)
            if not msg:
                break
            
            self.request.send(msg)
            print(msg.decode('utf-8'))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Send and recive UDP,' 'pretending packet are often dropped')
    parser.add_argument('-p', metavar='PORT', type=int, default=8080, help='UDP port(default 8080)')
    args = parser.parse_args()
    serv = TCPServer(('', args.p), EchoHandler)
    serv.serve_forever()
