import time
import board
from analogio import AnalogIn
import pwmio
pin = AnalogIn(board.A1)
motor = pwmio.PWMOut(board.D5)
while True: 

    print(pin.value)
    time.sleep(0.1)
    motor.duty_cycle = pin.value
