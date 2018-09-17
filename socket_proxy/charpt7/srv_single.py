import zen_utils

if __name__ == '__main__':
    address = zen_utils.parse_command_line('simple siggle-threaded server')
    listener = zen_utils.create_srv_socket(address)  # type: object
    zen_utils.accept_connections_forever(listener)