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
		self.min_distance = 20




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

		'''
		Directions Tuples
		Foward = (True, False)
		Backward = (False, True)
		Right = (False, False)
		Left = () 
		'''


		## Start Movement Loop ##
		while True:
			print("Direction: ", self.direction)
			self.distance = self.sonar.getDistance()
			## Check if Distance is greater than minimun ##
			if self.distance > self.min_distance:
				self.direction = 'w'

			## If distance > min, than move fowards ##
			if self.distance > self.min_distance and self.direction == 'w':
				while self.distance > self.min_distance:

					self.distance = self.sonar.getDistance() ## Get distance
				## Method Atributes
				#gpiopins, wait=.001, steps=512, ccwise=False,verbose=False, 
				#steptype="half", initdelay=.001)
					self.motor_1.motor_run(self.motor_1_pins,.001, 1,True,
		                  False,"half",0) ## 1 Step for motor 1 
					self.motor_2.motor_run(self.motor_2_pins,.001, 1,False,
		                  False,"half",0) ## 1 step for motor 2
				self.direction = 's'
				print("Distance less than minimun, going backward and turn")

			#time.sleep(0.05)
			self.distance = self.sonar.getDistance() ## Check Distance Again
			
			####################################################################
			### Check if distance is

			if self.distance < self.min_distance and self.direction!='p':
				print("Avoiding Mode On")

				if self.direction == 's':
					print("Going backward 1/2 wheel turn")
					for i in range(256):
						self.motor_1.motor_run(self.motor_1_pins,.005, 1,False,
			                  False,"half",0) ## 1 Step for motor 1 
						self.motor_2.motor_run(self.motor_2_pins,.005, 1,True,
			                  False,"half",0) ## 1 step for motor 2
						
					self.direction='d'

				self.distance = self.sonar.getDistance() ## Check Distance Again
				print("Distance: ", self.distance)

				## Turn 45 degrees to Right##
				if self.direction == 'd':
					print('Start Turning: ', self.direction)
					for i in range(64):
						self.motor_1.motor_run(self.motor_1_pins,.001, 1,False,
			                  False,"half",0) ## 1 Step for motor 1 
						self.motor_2.motor_run(self.motor_2_pins,.001, 1,False,
			                  False,"half",0) ## 1 step for motor 2
				





			

		





