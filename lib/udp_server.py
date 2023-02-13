import socket
import select
import time
import uasyncio

def startUDPServer(server, port, buffer_size):
    
    msgFromServer = 'Hello UDP Client'
    bytesToSend = str.encode(msgFromServer)

    # Create a datagram socket
    UDPServerSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # Bind to address and ip
    UDPServerSocket.bind((server, int(port)))
    print("Starting UDP Server")
    try:
#         poller = select.poll()
#         poller.register(server, select.POLLIN)
#         res = poller.poll(15000)  # time in milliseconds
#         if not res:
#             return None
#         else:   
    # Listen for incoming datagrams
            while True:
                bytesAddressPair = UDPServerSocket.recvfrom(int(buffer_size))
                message = bytesAddressPair[0]
                address = bytesAddressPair[1]

                clientMsg = 'Message from Client:{}'.format(message)
                clientIP = 'Client IP Address:{}'.format(address)
                print (clientMsg, clientIP)

                # Sending a reply to client
                UDPServerSocket.sendto(bytesToSend, address)
                send = 0
    except OSError as e:
        print("Couldnt connect to UDP Server")
        time.sleep(5)