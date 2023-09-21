# Write your code here :-)
# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
from adafruit_motor import servo
from digitalio import DigitalInOut, Direction, Pull


# Create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

#button 1 turns to 180
btn = DigitalInOut(board.D11)
btn.direction = Direction.INPUT
btn.pull = Pull.DOWN

#button 2 turns to 0
btn2 = DigitalInOut(board.D6)
btn2.direction = Direction.INPUT
btn2.pull = Pull.DOWN

while True:
    # if button 1 is pressed then it will turn to 180
    if btn.value:
        my_servo.angle = 180
        time.sleep(0.02 )
        print("BTN1 is pressed") 
        # if button 2 is pressed it will turn to 0
    if btn2.value:
        my_servo.angle = 0
        time.sleep(0.05)
        print("BTN2 is pressed")

