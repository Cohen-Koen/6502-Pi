#!/usr/bin/python
import time
import RPi.GPIO as g
g.setmode(g.BOARD)

dfpn = [3,5,7,11,13,15,19,21,23,29,31,33]
def cpinset(cpin):
    cpin = g.setup(cpin, g.OUT) #set clockpin, useful for setup


def clock(pin, mhz, pn , debug):   # clock program, take MHZ and pin then proceeds to flash it
    cpinset(pin)
    while True:
        time.time()
        delay = 1 / (mhz * 1000000)

        g.output(pin, 1)

        time.sleep(delay/2)
        g.output(pin, 0)

        time.sleep(delay/2)

        if debug == True: rdaddr(pn)



def off(pin): #inits the pin and turns it off
    cpinset(pin)
    g.output(pin,0)


def initin(pn):
        for i in range(len(pn)):
            g.setup(pn[i], g.IN)

def rdaddr(pn):
    aout = ""
    for i in range(len(pn)):
        bit = g.input(pn[i])
        bit = 0 if bit == False else 1
        aout += str(bit)
    print(aout, '\n')   #inspired by eaters approach on his arduino
