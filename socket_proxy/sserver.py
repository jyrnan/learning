from socket import socket, AF_INET, SOCK_STREAM
import argparse
import requests
import sys

def echo_handler(address, client_sock):
    print('Got connection from {}'.format(address))
    data = b''
    while True:
        msg = client_sock.recv(8192)
        if not msg:
            break
        data = data + msg
    sys.stdout.flush()
    print(data.decode('ascii')) 
    url = data.decode('ascii')
    try:
        rsp = requests.get(url).content
        client_sock.sendall(rsp)
        print('Content returned!')
    finally:
        client_sock.close()
    print('disconnected from {}'.format(address))

def echo_server(address, backlog=5):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(backlog)
    while True:
        print('Waiting for connection...')
        client_sock, client_addr = sock.accept()
        echo_handler(client_addr, client_sock)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Send and recive UDP,' 'pretending packet are often dropped')
    parser.add_argument('-p', metavar='PORT', type=int, default=8080, help='UDP port(default 8080)')
    args = parser.parse_args()
    echo_server(('', args.p))
