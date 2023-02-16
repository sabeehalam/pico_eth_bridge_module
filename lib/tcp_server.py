import request_to_json
import time
import select
import socket

#Open Socket
def openSocket(port):
    try:
        address = socket.getaddrinfo('0.0.0.0', port)[0][-1]
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_socket.bind(address)
        tcp_socket.listen(5)
#         server.settimeout(0)
#         server.setblocking(False)
        print('listening on', address)
        return tcp_socket
    except TypeError as e:
        print("Socket not established")
        return "Not found"

#Connect client to tcp server
def listenTCPServer(tcp_socket, buffer_size):
    if(tcp_socket == "No found"):
        return 1,1
    try:
        poller_tcp = select.poll()
        poller_tcp.register(tcp_socket, select.POLLIN)
        request = poller_tcp.poll(1000)  # time in milliseconds
        if not request:
            pass
        else:
#             # bind the socket to the port
#             socket.bind(host_1)
#             # listen for incoming connections
#             socket.listen(5)
# #         sock_1.setblocking(False) #Set sockets to non-blocking
#             print("Server started...")

        # sockets from which we expect to read
            inputs = [tcp_socket]
            outputs = []

            while inputs:
                # wait for at least one of the sockets to be ready for processing
                readable, writable, exceptional = select.select(inputs, outputs, inputs)

                for s in readable:
                    if s is tcp_socket:
                        conn, addr = s.accept()
                        inputs.append(conn)
                    else:
                        data = s.recv(buffer_size)
                        if data:
                            print(data)
                            respondTCPServer(conn, data, response)
                        else:
                            inputs.remove(s)
                            s.close()                

    except TypeError as e:
        print("Couldn't find any client for TCP server")


def respondTCPServer(client, request, response):
    try:
        client.sendall('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        client.sendall(response)
        params = request_to_json.parameterSort(str(request))
        print(params)
        request_to_json.saveVariables(params)
        request_to_json.savePreviousVariables(params)
        request_to_json.printParameters()
        client.close()       
        print("Connection closed")
        
    except OSError as e:
        print("Couldn't respond to client from tcp server")
