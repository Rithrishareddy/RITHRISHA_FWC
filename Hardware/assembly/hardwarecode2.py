from machine import Pin
from time import sleep

# Input buttons
P = Pin(10, Pin.IN, Pin.PULL_DOWN)
Q = Pin(11, Pin.IN, Pin.PULL_DOWN)
R = Pin(12, Pin.IN, Pin.PULL_DOWN)
S = Pin(13, Pin.IN, Pin.PULL_DOWN)

# Output LED
LED = Pin(15, Pin.OUT)

while True:
    p = P.value()
    q = Q.value()
    r = R.value()
    s = S.value()

    # Logic: F = P'R'S + PQ'R + PRS + P'QR'
    term1 = (not p) and (not r) and s
    term2 = p and (not q) and r
    term3 = p and r and s
    term4 = (not p) and q and (not r)

    F = term1 or term2 or term3 or term4

    LED.value(F)

    sleep(0.1)
