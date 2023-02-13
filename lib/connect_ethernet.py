import network
import socket
import time
from machine import Pin

#Create connection to ethernet 
def makeConnection(nic, parameters):
    
    nic.active(True)
    #None DHCP
    nic.ifconfig((parameters['Server'],'255.255.255.0','192.168.0.1','8.8.8.8'))
    #DHCP
    # nic.ifconfig('dhcp')
    print('IP address :', nic.ifconfig())
    
    # Wait for connect or fail
    max_wait = 10
    while max_wait > 0:
        if nic.isconnected() == 1:
            break
        max_wait -= 1
        print('waiting for connection...')
        time.sleep(1)

    # Handle connection error
    if nic.isconnected() == 0:
        raise RuntimeError('network connection failed')
    else:
        print('connected')
        status = nic.ifconfig()
        print( 'ip = ' + status[0] )
    
    return nic

def checkConnection(nic):
    while not nic.isconnected():
        time.sleep(1)   
        print(nic.regs())

def reconnectConn(nic):
    reset = Pin(30)
    reset.on()
    time.sleep_us(600)
    nic.active("False")
    reset.off()