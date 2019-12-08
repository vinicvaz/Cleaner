import RPi.GPIO as GPIO
import time
from RpiMotorLib import RpiMotorLib
from Control import Control_Class
from Sonar import SonarClass
from Servo import ServoClass

## in1,in2,in3,in4 
GPIO_PINS_1 = [25,24,23,6] ## Motor 1 Pins
GPIO_PINS_2 = [26,16,5,12] ## Motor 2 Pins


#####################
#### MOTOR SETUP ####
#####################
motor_1 = RpiMotorLib.BYJMotor("Motor1", "28BYJ")
motor_2 = RpiMotorLib.BYJMotor("Motor2", "28BYJ")

###### SETUP SONARS ######
sonar = SonarClass(22,27) ## Sonar Pins
sonar_servo = SonarClass(17,18) ## Sonar Servo PIns

###### Setup Servo ######
servo = ServoClass(13)

control = Control_Class(motor_1,motor_2,[25,24,23,6],[26,16,5,12],sonar, sonar_servo, servo)

#control.start_movement()

#control.movement()
