from machine import Pin
from time import sleep

# Define input pins
Y = Pin(10, Pin.IN, Pin.PULL_DOWN)
Z = Pin(11, Pin.IN, Pin.PULL_DOWN)

# Fixed input
X = 1

# Output LED
LED = Pin(15, Pin.OUT)

while True:
    y = Y.value()
    z = Z.value()

    # Compute expression
    # E = (X + Z * (~Y + ~Z + X * ~Y)) * (~X + ~Z * (X + Y))
    notY = int(not y)
    notZ = int(not z)
    notX = int(not X)

    # Break down expression
    inner1 = notY or notZ or (X and notY)
    part1 = X or (z and inner1)

    inner2 = X or y
    part2 = notX or (notZ and inner2)

    result = part1 and part2

    LED.value(result)

    sleep(0.1)
