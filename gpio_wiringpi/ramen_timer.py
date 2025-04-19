
#coding: utf-8

import sys
import wiringpi as pi
import time

# pin numbers
SW_PIN = 24
BUZZER_PIN = 23
LED_PIN = 18

# pin setting
pi.wiringPiSetupGpio()
pi.pinMode(LED_PIN, pi.OUTPUT)
pi.pinMode(SW_PIN, pi.INPUT)
pi.pinMode(BUZZER_PIN, pi.OUTPUT)

# test
pi.digitalWrite(BUZZER_PIN, pi.HIGH)
time.sleep(0.5)
pi.digitalWrite(BUZZER_PIN, pi.LOW)


def is_sw_pushed():
    return pi.digitalRead(SW_PIN) == pi.LOW

def waiting_input():
    while True:
        if(is_sw_pushed()):
            return True
        time.sleep(0.1)


def timer_counting(duration):
    elapsed_time = 0
    # while(elapsed_time < 180):
    while(elapsed_time < duration):
        # if (is_sw_pushed()): elapsed_time = 0
        pi.digitalWrite(LED_PIN, pi.HIGH)
        time.sleep(0.2)
        pi.digitalWrite(LED_PIN, pi.HIGH)
        time.sleep(0.8)
        elapsed_time += 1

    return True

def calling_buzzer():
    while True:
        pi.digitalWrite(BUZZER_PIN, pi.HIGH)
        time.sleep(0.1)
        if (is_sw_pushed()):
            break
    pi.digitalWrite(BUZZER_PIN, pi.LOW)

    return True

def main():
    try:
        # if(is_sw_pushed()):
        while True:
            waiting_input()
            timer_counting(3)
            calling_buzzer()
    except KeyboardInterrupt:
        print("Interrupted.")
        sys.exit(0)

    return 0


if __name__ == "__main__":
    main()



# pi.pullUpDnControl(SW_PIN, pi.PUD_UP)

# while True:
#     if(pi.digitalRead(SW_PIN) == pi.LOW):
#         pi.digitalWrite(LED_PIN, pi.HIGH)
#     else:
#         pi.digitalWrite(LED_PIN, pi.LOW)
#     time.sleep(0.1)



# while True:
#     if (pi.digitalRead(SW_PIN) == pi.LOW):
        
#     else:
#         pi



# state 1: wait to set timer
# state 2: counting timer
# state 3: turn on buzzer and led blink

