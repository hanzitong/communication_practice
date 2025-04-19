
#coding: utf-8

import wiringpi as pi
import time

LED_PIN = 23
SW_PIN = 24
BUZZER_PIN = 23

pi.wiringPiSetupGpio()
pi.pinMode(LED_PIN, pi.OUTPUT)
pi.pinMode(SW_PIN, pi.INPUT)
pi.pinMode(BUZZER_PIN, pi.OUTPUT)

pi.digitalWrite(BUZZER_PIN, pi.HIGH)
# time.sleep(0.5)
pi.digitalWrite(BUZZER_PIN, pi.LOW)
# time.sleep(0.5)

# state = 1

def is_sw_pushed():
    pin_state = pi.digitalRead(SW_PIN)
    if(pin_state == pi.LOW):
        return True
    else:
        return False

def waiting_input():
    while True:
        if(is_sw_pushed): return True
        time.sleep(0.1)

    return False

# def state_running_timer():
def timer_counting():
    elapsed_time = 0
    while(elapsed_time < 180):
        if (is_sw_pushed()): elapsed_time = 0
        time.sleep(1)
        elapsed_time += 1

    return True

def calling_buzzer():
    while True:
        pi.digitalWrite(BUZZER_PIN, pi.HIGH)
        if (is_sw_pushed()): break

    return True

def main():
    try:
        # if(is_sw_pushed()):
        while True:
            waiting_input()
            timer_counting()
            calling_buzzer()
    except KeyboardInterrupt:
        sys.exit(0)

    return 0





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

