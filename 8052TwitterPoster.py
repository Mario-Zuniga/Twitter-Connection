import time
import serial
from twitter import *
from twython import Twython

#https://twitter.com/8052MicroLopez
#marioalex

serConnection = serial.Serial(
    port='COM1',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

config = {}
execfile("config.py", config)

twitter = Twython(config['token'], config['token_key'], config['con_secret'], config['con_secret_key'])
def tweet_message(message):
    twitter.update_status(status=message)
    print("Status posted")
    time.sleep(5)

print("Application running...")
while(True):

    print("Awaiting serial input...")

    message = ""

    while serConnection.inWaiting() > 0:
        message += serConnection.read(1)
		
    if message != "" and message[-1] == "*":
        tweet_message(message[0:-1])
        print(message[0:-1])

    time.sleep(1)
