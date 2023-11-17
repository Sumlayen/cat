from adafruit_servokit import ServoKit
import time
import sys

kit = ServoKit(channels=16)
# kit.servo[0].set_pulse_width_range(900, 2100)

def spin():
    # time.sleep(2)
    kit.servo[0].angle = 150
    # print('reset')
    time.sleep(.2)

    kit.servo[0].angle = 110
    # print('Turn')
    time.sleep(.5)
    kit.servo[0].angle = 150
    # print('reset again')
    # i = i + 1
