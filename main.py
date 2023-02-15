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

while True:
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
        
        if(CONNECT_WEBSERVER == 0):
            web_server_socket = web_server.openSocket(int(params["ServerPort"]))
            web_server.listenWebServer(web_server_socket, params["BufSize"])
            CONNECT_WEBSERVER = 1
         
        if(CONNECT_WEBSERVER == 1):
            web_server.listenWebServer(web_server_socket, response)
    
        if(params["Protocol"] == "TCP-SERVER"):
            if(CONNECT_TCP_SERVER == 0):
                tcp_server_socket = tcp_server.openSocket(params["LocalPort"])
                tcp_server.listenTCPServer(tcp_server_socket, params["BufSize"])
                CONNECT_TCP_SERVER = 1
                
        if(CONNECT_TCP_SERVER == 1):
                tcp_server.listenTCPServer(tcp_server_socket, params["BufSize"])

            
#         if(params["Protocol"] == "TCP-CLIENT"):
#             tcp_client.startTCPClient(params["Server"], params["LocalPort"], params["BufSize"])        
#         if(params["Protocol"] == "UDP-CLIENT"):
#             udp_client.startUDPClient(params["Server"], params["LocalPort"], params["BufSize"])
#         if(params["Protocol"] == "UDP-SERVER"):
#             udp_server.startUDPServer(params["Server"], params["LocalPort"], params["BufSize"])
#         if(params["Protocol"] == "MQTT-CLIENT"):
#             mqtt_client.startMQTTClient(params["MqClientID"], params["Server"], params["MqUSER"],\
#                             params["MqPasswd"], params["KeepAlive"], params["LocalPort"])
#         
#         event_loop = asyncio.get_event_loop()
#         event_loop.run_until_complete(asyncio_functions.uasyncioConnectConfig(params, response))
#         event_loop.run_until_complete(asyncio_functions.uasyncioTCPServer(params, response))
#         event_loop.run_forever()
#         
        gc.collect()
 
    except KeyboardInterrupt as e:
#     client.close()
        print('Keyboard Interrupt called')
        break
