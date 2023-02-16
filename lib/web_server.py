import request_to_json
import time
import select
import socket

#Open Socket
def openSocket(port):
    try:
        address = socket.getaddrinfo('0.0.0.0', port)[0][-1]
        web_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        web_socket.bind(address)
        web_socket.listen(5)
#         web_socket.settimeout(0)
#         web_socket.setblocking(False)
        print('listening on', address)
        return web_socket
    except TypeError as e:
        print("Socket not established")
        return web_socket

#Connect client to web server
def listenWebServer(web_socket, buffer_size, response):
    if(web_socket == "No found"):
        return 1,1
    try:
#         poller_web = select.poll()
#         poller_web.register(web_socket, select.POLLIN)
#         request = poller_web.poll(1000)  # time in milliseconds
#         if not request:
#             pass
#         else:
#             # bind the socket to the port
#             socket.bind(host_1)
#             # listen for incoming connections
#             socket.listen(5)
# #         sock_1.setblocking(False) #Set sockets to non-blocking
#             print("Server started...")

        # sockets from which we expect to read
            inputs = [web_socket]
            outputs = []

            while inputs:
                # wait for at least one of the sockets to be ready for processing
                readable, writable, exceptional = select.select(inputs, outputs, inputs)

                for s in readable:
                    if s is web_socket:
                        conn, addr = s.accept()
                        inputs.append(conn)
                    else:
                        data = s.recv(buffer_size)
                        if data:
                            print(data)
                            respondWebServer(conn, data, response)
                            s.close()
                            print("Client closed")
                        else:
                            inputs.remove(s)
                            s.close()                

    except OSError as e:
        print("Couldn't find any client for web server")


def respondWebServer(client, request, response):
    try:
        client.sendall('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        client.sendall(response)
        params = request_to_json.parameterSort(str(request))
        print(params)
        request_to_json.saveVariables(params)
        request_to_json.savePreviousVariables(params)
        request_to_json.printParameters()
        
    except OSError as e:
        print("Couldn't respond to client from web server")