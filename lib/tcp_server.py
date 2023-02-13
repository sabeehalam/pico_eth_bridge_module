import socket
import select
import uasyncio
import time

#Open Socket
def openSocket(port):
    try:
        addr = socket.getaddrinfo('192.168.0.110', int(port))[0][-1]
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(addr)
        server.listen(1)
        server.setblocking(False)
    except OSError as e:
        print("Socket not established")
        time.sleep(5)
    print('listening on', addr)
    return server
   
def checkAndSendBuffer(server, buffer_size):
    try:
        rlist, _, _ = select.select([server], [], [], 1)
        if rlist:
            client, address = server.accept()
            try:
                request = client.recv(int(buffer_size))
                response = "Connected to TCP Server"
                client.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
                client.send(response)
                client.close()
            except OSError as e:
                print("Data Sent to client")
    except OSError as e:
        print("No client found")
        