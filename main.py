import os
from machine import Pin, SPI
import network
import socket
import uasyncio as asyncio
import time
import gc
import select
import pico_html
import request_to_json
import connect_ethernet
import web_server
import mqtt_client
import tcp_client
import tcp_server
import udp_client
import udp_server
import asyncio_functions

#Ethernet Connection constants
SPI_ID = 1
SCK    = Pin(10)
MOSI   = Pin(11)
MISO   = Pin(12)
CSN    = Pin(13)
RESET  = Pin(15)

CONNECT_WEBSERVER  = 0
WEBSERVER_PORT     = 80
CONNECT_TCP_SERVER = 0

try:
    spi = SPI(SPI_ID, 20000, mosi=MOSI, miso=MISO, sck=SCK) #SPI Intialization
    nic = network.WIZNET5K(spi,CSN,RESET) #spi,csn,reset pin #Wiznet intiialization
except OSError:
    print("Couldn't declare Wiznet parameters")

response = pico_html.getHTML() #import the webpage to be hosted
params = request_to_json.loadParameters()

try:
    nic = connect_ethernet.makeConnection(nic, params) #Initiate connection of pico via ethernet for web server hosting
except OSError:
    print("Couldn't connect to the Ethernet")

# Runs a loop open web server and tcp server sockets and listen for connections.
# If request arrives, respond to them
#Problem: Can only poll one at a time

try:
    params = request_to_json.loadParameters()
        
    if params["Server"] == "":
        params["Server"] = "192.168.0.110"
    if params["ServerPort"] == "":
        params["ServerPort"] = "1880"
    if params["BufSize"] == "":
        params["BufSize"] = "1024"
    if params["LocalPort"] == "":
        params["LocalPort"] = "1883"
        
    #Declare and open web server socket
    try:
        web_server_socket = web_server.openSocket(int(params["ServerPort"]))
        CONNECT_WEBSERVER = 1
    except TypeError as e:
        CONNECT_WEBSERVER = 0
        
    #Declare and open tcp server socket
    try:
        if(params["Protocol"] == "TCP-SERVER"):
            if(CONNECT_TCP_SERVER == 0):
                tcp_server_socket = tcp_server.openSocket(params["LocalPort"])
                CONNECT_TCP_SERVER = 1
    except TypeError as e:
        CONNECT_TCP_SERVER = 0
            
    # Create a list of sockets to monitor
    socks = [web_server_socket, tcp_server_socket]
        
    # Create a selector object and register the sockets
    sel = select.poll()
    for s in socks:
        sel.register(s, select.POLLIN)
            
    # Loop indefinitely, waiting for events on the sockets
    while True:
        # Wait for events on the sockets
        events = sel.poll()

        # Process the events
        for sock, event in events:
            if sock == web_server_socket:
                listenWebServer(params["Server"], params["ServerPort"], params["BufSize"])
            elif sock == tcpserver:
                listenTCPServer(params["Server"], params["LocalPort"], params["BufSize"])
            elif event & select.POLLIN:
                # There is data to read on a socket
                data = sock.recv(1024)
                if not data:
                    # The remote host has closed the connection
                    sel.unregister(sock)
                    sock.close()
                else:
                    # Process the data
                    print(data)
                    # Check if the socket is the webserver
                    if sock == web_server_socket:
                        respondWebServer(client, request, response)
                          
#         if(params["Protocol"] == "TCP-CLIENT"):
#             tcp_client.startTCPClient(params["Server"], params["LocalPort"], params["BufSize"])        
#         if(params["Protocol"] == "UDP-CLIENT"):
#             udp_client.startUDPClient(params["Server"], params["LocalPort"], params["BufSize"])
#         if(params["Protocol"] == "UDP-SERVER"):
#             udp_server.startUDPServer(params["Server"], params["LocalPort"], params["BufSize"])
#         if(params["Protocol"] == "MQTT-CLIENT"):
#             mqtt_client.startMQTTClient(params["MqClientID"], params["Server"], params["MqUSER"],\
#                             params["MqPasswd"], params["KeepAlive"], params["LocalPort"])

        gc.collect()
 
    except KeyboardInterrupt as e:
#     client.close()
        print('Keyboard Interrupt called')
        break
