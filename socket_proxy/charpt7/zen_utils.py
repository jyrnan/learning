#!/usr/bin/env python3

import argparse, socket, time

aphorisms = {b'Beautiful is better than?': b'Ugly.',
			b'Explicit is better than?': b'Implicit.',
			b'Simple is better than?': b'Complex.'}


def get_answer(aphorism):
	
	time.sleep(0.0) # increase to simulate an expensive operation
	return aphorisms.get(aphorism, b'Error: unknow aphorism.')

	
def parse_command_line(description):
	
	parser = argparse.ArgumentParser(description=description)
	parser.add_argument('host', help='IP or hostname')
	parser.add_argument('-p', metavar='port', type=int, default=1060, help='TCP port (default 1060)')
	args = parser.parse_args()
	address = (args.host, args.p)
	return address


def create_srv_socket(address):
	"""build and return a listening server socket"""
	listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	listener.bind(address)
	listener.listen(64)
	print('Listening at {}'.format(address))
	return listener


def accept_connections_forever(listener):
	"""Forever answer income connections on a listening socket."""
	while True:
		sock, address = listener.accept()
		print('Accepted connection from {}'.format(address))
		handle_conversation(sock, address)


def handle_conversation(sock, address):
	"""`converse with a client over 'sock' untill they are done talking"""
	try:
		while True:
			handle_request(sock)
	except EOFError:
		print('Client socket to {} has closed'.format(address))
	except Exception as e:
		print('Client {} error {}'.format(address, e))
	finally:
		sock.close()


def handle_request(sock):
	"""recieve a sigle client request on 'sock' and the answer"""
	aphorism = recv_until(sock, b'?')
	# print('aphorism is: ', aphorism) # added by myself for testing
	answer = get_answer(aphorism)
	# print('anwser is :', answer) # added by myself for testing
	sock.sendall(answer)


def recv_until(sock, suffix):
	"""recive bytes over socket 'sock' until we receive the 'suffix'. """
	message = sock.recv(4096)
	# print(message) # added by myself for testing
	if not message:
		raise EOFError('socket closed')
	while not message.endswith(suffix):
		data = sock.recv(4096)
		if not data:
			raise IOError('recived {!r} then socket closed'.format(message))
		message += data
	return message