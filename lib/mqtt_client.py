from umqtt.simple import MQTTClient
from time import sleep
import uasyncio

'''Connect to MQTT Broker'''
def startMQTTClient(client, broker, user, password, keep_alive, port):
    try:
            print("Connecting to MQTT server... ", end="")
            client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD, \
                        keepalive = KEEP_ALIVE_DURATION, port = MQTT_PORT)
            client.connect()
            print("Connected!")
            
    except Exception as e:
            print("Error in mqtt connect: [Exception] %s: %s" % (type(e).__name__, e))
            sleep(0.5) # to brake the loop
    return client

