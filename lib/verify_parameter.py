import uasyncio
import request_to_json

async def checkVariables(params):
    if params["Server"] == "":
        params["Server"] = "192.168.0.110"
    if params["ServerPort"] == "":
        params["ServerPort"] = "80"
    if params["BufSize"] == "":
        params["BufSize"] = "1024"
    if params["LocalPort"] == "":
        params["LocalPort"] = "1880"
            
    await uasyncio.sleep(1)
    
async def checkProtocol(protocol):
    if(protocol == "TCP-CLIENT"):
        tcp_client.startTCPClient(params["Server"], params["LocalPort"], params["BufSize"])
    if(protocol == "TCP-SERVER"):
        tcp_server.startTCPServer(params["Server"], params["LocalPort"], params["BufSize"])
    if(protocol == "UDP-CLIENT"):
        udp_client.startUDPClient(params["Server"], params["LocalPort"], params["BufSize"])
    if(protocol == "UDP-SERVER"):
        udp_server.startUDPServer(params["Server"], params["LocalPort"], params["BufSize"])
    if(protocol == "MQTT-CLIENT"):
        mqtt_client.startMQTTClient(params["MqClientID"], params["Server"], params["MqUSER"],\
                            params["MqPasswd"], params["KeepAlive"], params["LocalPort"])
    await uasyncio.sleep(1)    
    