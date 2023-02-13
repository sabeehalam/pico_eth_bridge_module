import socket
import uasyncio

def startUDPClient(server, port, buffer_size):
    print("UDP Client started")
    msgFromClient = 'Hello UDP Server'
    bytesToSend = str.encode(msgFromClient)
    serverAddressPort = (server, int(port))

    # Create a UDP socket at client side
    UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        # Send to server using created UDP socket
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    
        print("UDP client waiting")
        msgFromServer = UDPClientSocket.recvfrom(int(buffer_size))
        msg = 'Message from Server {}'.format(msgFromServer[0])
        print(msg) 