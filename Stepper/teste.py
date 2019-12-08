import RPi.GPIO as GPIO
import time
from RpiMotorLib import RpiMotorLib

## in1,in2,in3,in4 
GPIO_PINS_1 = [25,24,23,6] ## Motor 1 Pins
GPIO_PINS_2 = [26,16,5,12] ## Motor 2 Pins


motor_1 = RpiMotorLib.BYJMotor("Motor1", "28BYJ")
motor_2 = RpiMotorLib.BYJMotor("Motor2", "28BYJ")

for i in range(512):
	motor_1.motor_run(gpiopins=GPIO_PINS_1, wait=.01, steps=1, ccwise=False,
	                  verbose=True, steptype="half", initdelay=0)
	motor_2.motor_run(gpiopins=GPIO_PINS_2, wait=.01, steps=1, ccwise=True,
	                  verbose=True, steptype="half", initdelay=.0)
