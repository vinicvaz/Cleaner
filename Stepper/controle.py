import RPi.GPIO as GPIO
import time
from RpiMotorLib import RpiMotorLib

class Control_Class:

	def __init__(self, motor_1,motor_2,motor_1_pins, motor_2_pins, sonar):

		###### Motors Init ######
		self.motor_1 = motor_1
		self.motor_2 = motor_2
		self.motor_1_pins = motor_1_pins
		self.motor_2_pins = motor_2_pins
		########################
		###### Sonar Init #####
		self.sonar = sonar
		######################


		###### Variables #####
		self.distance = sonar.getDistance()

		###### Values ######
		self.min_distance = 40



	def moves(self):
		print("Checking Distance to move")
		self.distance=self.sonar.getDistance()
		print("Start Distance:", self.distance)
		time.sleep(2)
		if self.distance < self.min_distance:
			print("No way to move")
		





