import RPi.GPIO as GPIO
import time
from RpiMotorLib import RpiMotorLib

class Control_Class:

	def __init__(self, motor_1,motor_2,motor_1_pins, motor_2_pins, sonar, sonar_servo, servo):

		###### Motors Init ######
		self.motor_1 = motor_1
		self.motor_2 = motor_2
		self.motor_1_pins = motor_1_pins
		self.motor_2_pins = motor_2_pins
		########################
		###### Sonar Init ######
		self.sonar = sonar
		self.sonar_servo = sonar_servo
		######################
		###### Servo Init ####
		self.servo = servo


		###### Variables #####
		self.turn = 64 ## Steps to Turn
		self.servo_angle = {"right":0,"center":90,"left":180} ## Servo Angle Dict
		self.distance = sonar.getDistance()
		self.direction = 'n' ## w = foward, s=backward, d=right turn, l=left turn, p=stop, n=none
		###### Fix Values ######
		self.min_distance = 15
		self.warning_distance = 25