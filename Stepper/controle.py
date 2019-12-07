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
		self.direction = 'n' ## w = foward, s=backward, d=right turn, l=left turn, p=stop, n=none
		###### Fix Values ######
		self.min_distance = 45
		self.car_size = 30




	def start_movement(self):
		print("Checking Distance to move")
		self.distance=self.sonar.getDistance()
		print("Start Distance:", self.distance)
		time.sleep(2)
		if self.distance < self.min_distance:
			print("No way to move")
			self.direction='p'
		else:
			print("Starting Movement Foward")
			self.direction = 'w'


	def movement(self):
		print("Started with direction: ", self.direction)

		while True:

			self.distance = self.sonar.getDistance()
			## Check if Distance
			if self.distance > self.min_distance:
				self.direction = 'w'

			if self.distance > self.min_distance and self.direction == 'w':
				while self.distance > self.min_distance:

					self.distance = self.sonar.getDistance() ## Get distance
				## Method Atributes
				#gpiopins, wait=.001, steps=512, ccwise=False,verbose=False, 
				#steptype="half", initdelay=.001)

					self.motor_1.motor_run(self.motor_1_pins,.001, 1,True,
		                  False,"half",0) ## 1 Step for motor 1 
					self.motor_2.motor_run(self.motor_2_pins,.001, 1,True,
		                  False,"half",0) ## 1 step for motor 2
					time.sleep(0.005)
				self.direction = 's'
				print("Distance less than minimun, going backward and turn")

			time.sleep(0.05)
			self.distance = self.sonar.getDistance() ## Check Distance

			if self.distance < self.min_distance and self.direction!='p':
				print("Going backward 1 wheel turn")
				if self.direction == 's':
					for i in range(512):
						self.motor_1.motor_run(self.motor_1_pins,.001, 1,False,
			                  False,"half",0) ## 1 Step for motor 1 
						self.motor_2.motor_run(self.motor_2_pins,.001, 1,False,
			                  False,"half",0) ## 1 step for motor 2
						time.sleep(0.005)
					self.direction='d'
				self.distance = self.sonar.getDistance()
				print("Distance: ", self.distance)
				print('Start Turning: ', self.direction)
				## Turn 45 degrees ##
				if self.direction == 'd':
					for i in range(64):
						self.motor_1.motor_run(self.motor_1_pins,.001, 1,True,
			                  False,"half",0) ## 1 Step for motor 1 
						self.motor_2.motor_run(self.motor_2_pins,.001, 1,False,
			                  False,"half",0) ## 1 step for motor 2
						time.sleep(0.005)				




			

		





