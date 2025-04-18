
#coding: utf-8

import wiringpi as pi
import time

LED_PIN = 23

pi.wiringPiSetupGpio()
pi.pinMode(LED_PIN, pi.OUTPUT)
pi.softWwmCreate(LED_PIN, 0, 100)

# while True:
#     brightness = 0
#     while (brightness < 100):
#         pi.softPwmWrite(LED_PIN, brightness)
#         time.sleep(0.1)
#         brightness = brightness + 1
#     while (brightness > 0):
#         pi.softPwmWrite(LED_PIN, brightness)
#         time.sleep(0.1)
#         brightness = brithtness - 1


brightness = 0
while True:
    pi.softPwmWrite(LED_PIN, brightness)
    time.sleep(0.1)
    if (brightness < 100):
        brightness = brightness + 1
    else:
        brightness = brightness - 1

