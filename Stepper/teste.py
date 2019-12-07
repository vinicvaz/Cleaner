import RPi.GPIO as GPIO
import time
from RpiMotorLib import RpiMotorLib

## in1,in2,in3,in4 
GPIO_PINS_1 = [25,24,23,6] ## Motor 1 Pins
GPIO_PINS_2 = [26,16,5,12] ## Motor 2 Pins


motor_1 = RpiMotorLib.BYJMotor("Motor1", "28BYJ")
motor_2 = RpiMotorLib.BYJMotor("Motor2", "28BYJ")

motor_1.motor_run(gpiopins=GPIO_PINS_1, wait=.001, steps=512, ccwise=False,
                  verbose=True, steptype="half", initdelay=.001)