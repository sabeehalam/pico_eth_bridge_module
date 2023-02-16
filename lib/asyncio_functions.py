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
import web_server
import mqtt_client
import tcp_client
import tcp_server
import udp_client
import udp_server

CONNECT_WEBSERVER  = 0
WEBSERVER_PORT     = 80
CONNECT_TCP_SERVER = 0

async def uasyncioConnectConfig(params, response):
    global CONNECT_WEBSERVER
    if(CONNECT_WEBSERVER == 0):
        try:
            server = web_server.openSocket(int(params["ServerPort"]))
            request, client = web_server.listenWebServer(server)
            CONNECT_WEBSERVER = 1
        except TypeError as e:
            print("Couldnt find web server")
        finally:
            await asyncio.sleep(10)
         
    if(CONNECT_WEBSERVER == 1):
        try:
            request, client = web_server.listenWebServer(server)
            web_server.respondWebServer(client, response)
        except TypeError as e:
            print("Couldnt find web server")
        finally:
            await asyncio.sleep(10)
    
async def uasyncioTCPServer(params, response):
    global CONNECT_TCP_SERVER
    if(params["Protocol"] == "TCP-SERVER"):
        if(CONNECT_TCP_SERVER == 0):
            try:
                server = tcp_server.openSocket(params["LocalPort"])
                request, client = tcp_server.listenTCPServer(server)
                tcp_server.respondTCPServer(server, response)
                CONNECT_TCPSERVER = 1
            except TypeError as e:
                print("Couldnt find TCP server")
            finally:
                await asyncio.sleep(10)
            
        if(CONNECT_TCP_SERVER == 1):
            try:
                request, client = tcp_server.listenTCPServer(server)
                tcp_server.respondTCPServer(server, response)
            except TypeError as e:
                print("Couldnt find TCP server")
            finally:
                await asyncio.sleep(10)
            