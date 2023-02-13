import request_to_json
import time
import select
import socket
import uasyncio

#Open Socket
def openSocket(port):
    try:
        addr = socket.getaddrinfo('192.168.0.110', port)[0][-1]
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(addr)
        server.listen(1)
        server.setblocking(False)
    except OSError as e:
        print("Socket not established")
    print('listening on', addr)
    return server

#Connect client to web server
def connectWebServer(server,response):
    try:
        rlist, _, _ = select.select([server], [], [], 1)
        if rlist:
            client, address = server.accept()
            print('client connected from', address)
            try:                      
                client.sendall('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
                client.sendall(response) 
                request = client.recv(1024) 
                params = request_to_json.parameterSort(str(request))
                print(params)
                request_to_json.saveVariables(params)
                request_to_json.savePreviousVariables(params)
                request_to_json.printParameters()
                client.close()
                
            except OSError as e:
                print("Data sent to client")
    except OSError as e:
        print("Couldn't find any client for web server")