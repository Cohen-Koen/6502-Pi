#!/usr/bin/python
import time
import RPi.GPIO as g
g.setmode(g.BOARD)
debug = False

def cpinset(cpin):
    cpin = g.setup(cpin, g.OUT) #set clockpin, useful for setup


def clock(pin, mhz, debug):   # clock program, take MHZ and pin then proceeds to flash it
    cpinset(pin)
    while True:
        time.time()
        delay = 1 / (mhz * 1000000)

        g.output(pin, 1)
        if(debug==True):     print('on')
        time.sleep(delay/2)
        g.output(pin, 0)
        if(debug == True):   print('off')
        time.sleep(delay/2)



def off(pin): #inits the pin and turns it off
    cpinset(pin)
    g.output(pin,0)
    
