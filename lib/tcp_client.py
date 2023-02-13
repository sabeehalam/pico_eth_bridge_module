import socket
import uasyncio

def startTCPClient(server, port, buffer_size):
    addr = socket.getaddrinfo(server, int(port))[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.sendall(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (server, port), 'utf8'))
    while True:
        data = s.recv(int(buffer_size))
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break
    s.close()
