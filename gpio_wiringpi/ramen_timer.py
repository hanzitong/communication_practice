#coding: utf-8

import sys
import time
import wiringpi as pi

# pin numbers
SW_PIN = 24
BUZZER_PIN = 23
LED_PIN_W = 18
LED_PIN_G = 25

# pin setting
pi.wiringPiSetupGpio()
pi.pinMode(LED_PIN_W, pi.OUTPUT)
pi.pinMode(LED_PIN_G, pi.OUTPUT)
pi.pinMode(BUZZER_PIN, pi.OUTPUT)
pi.pullUpDnControl(SW_PIN, pi.INPUT)

# test
# pi.digitalWrite(BUZZER_PIN, pi.HIGH)
# time.sleep(0.5)
# pi.digitalWrite(BUZZER_PIN, pi.LOW)


def is_sw_pushed():
    return pi.digitalRead(SW_PIN) == pi.LOW

def waiting_input():
    while True:
        print("waiting input")
        if(is_sw_pushed()):
            return True
        time.sleep(0.1)


def timer_counting(duration):
    elapsed_time = 1
    while(elapsed_time < duration):
        # if (is_sw_pushed()): elapsed_time = 0
        print("timer counting: {}".format(elapsed_time))
        pi.digitalWrite(LED_PIN_W, pi.HIGH)
        time.sleep(0.2)
        pi.digitalWrite(LED_PIN_W, pi.LOW)
        time.sleep(0.8)
        elapsed_time += 1
    pi.digitalWrite(LED_PIN_W, pi.LOW)
    return True

def calling_buzzer():
    while True:
        print("calling buzzer")
        pi.digitalWrite(LED_PIN_G, pi.HIGH)
        pi.digitalWrite(BUZZER_PIN, pi.HIGH)
        time.sleep(0.1)
        if (is_sw_pushed()):
            break
    pi.digitalWrite(BUZZER_PIN, pi.LOW)
    pi.digitalWrite(LED_PIN_G, pi.LOW)

    return True

def main():
    try:
        while True:
            waiting_input()
            timer_counting(180)
            calling_buzzer()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Interrupted.")
        sys.exit(0)

    return 0

if __name__ == "__main__":
    main()
