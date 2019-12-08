import RPi.GPIO as GPIO
import time
from RpiMotorLib import RpiMotorLib
import numpy as np

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
		self.servo.set_angle(90)


		###### Variables #####
		self.turn = 64 ## Steps to Turn
		self.distance_dict = {'right':None, 'center':None,'left':None} ## Servo Distance Dict
		self.servo_angle = {"right":0,"center":90,"left":180} ## Servo Angle Dict
		self.distance = sonar.getDistance() ## Distance from center sonar
		self.distance_dict['center'] = self.sonar_servo.getDistance() ## Distance from servo sonar
		#self.servo_checking = False ## If true, servo is checking wich side turn
		self.direction = 'n' ## foward, backward, right, left, pause, n=none
		self.last_direction = 'n'
		###### Fix Values ######
		self.min_distance = 20
		self.warning_distance = 30
		



	def sonar_mean(self, sonar):
		array = []
		for i in range(5):
			self.distance = sonar.getDistance()
			array.append(self.distance)
		return np.mean(array)


	def start_movement(self):
		print('Checking Distance to Move')
		## Get 3 reads of sonar
		self.distance = self.sonar_mean(self.sonar)
		self.distance_dict['center'] = self.sonar_mean(self.sonar_servo)
		print('Distance: ',self.distance)
		print('Servo Distance:', self.distance_dict['center'])

		### If distance less than min distance device will not start
		if self.distance < self.min_distance or self.distance_dict['center']<self.min_distance:
			print("No way to move foward")
			self.direction = 'pause'
			self.moves()
		else:
			print("Starting movement Foward") ## Else start moving foward
			self.direction = 'foward'
			self.moves()

	def moves(self):

		while True:
			self.distance = self.sonar.getDistance()
			self.distance_dict['center'] = self.sonar_servo.getDistance()

			#if self.direction == 'center' and self.distance>self.min_distance:
			#if self.distance > self.min_distance and self.distance_dict['center']>self.min_distance:
			if self.direction == 'center':
				self.direction = 'foward'

			if self.distance > self.min_distance and self.distance_dict['center']> self.min_distance and self.direction =='foward':
				self.move_foward()
			elif self.direction == 'right':
				self.move_right()
			elif self.direction == 'left':
				self.move_left()
			elif self.direction == 'backward':
				self.move_backward()
			else:
				self.direction = self.stop_movement()
			


	def move_foward(self):


		## Moves both motor foward ##
		self.motor_1.motor_run(self.motor_1_pins,.001, 1,True, 
			False,"half",0) ## 1 Step Foward for motor 1 
		self.motor_2.motor_run(self.motor_2_pins,.001, 1,False,
		    False,"half",0) ## 1 step Foward for motor 2

	def move_right(self):
		## Moves right ##


		##### Check if have anything left ###
		self.servo.set_angle(self.servo_angle['left'])
		time.sleep(0.5)
		self.distance_dict['left'] == self.sonar_mean(self.sonar_servo)
		time.sleep(0.5)
		self.servo.set_angle(self.servo_angle['center'])

		print("TO NO RIGHT")
		##### If have way left, turn nose right ##
		if self.distance_dict['left'] > self.min_distance:
		
			for i in range(256):
				self.motor_1.motor_run(self.motor_1_pins,.001, 1,False, False,"half",0)
				self.motor_2.motor_run(self.motor_2_pins,.001, 1,False, False,"half",0)
			self.last_direction = 'right'
			self.direction = 'center'
		else:
			self.last_direction='right'
			self.direction = 'backward'

	def move_left(self):
		######### Moves left  ######### 

		##### Check if have anything right ###
		self.servo.set_angle(self.servo_angle['right'])
		time.sleep(0.5)
		self.distance_dict['right'] == self.sonar_mean(self.sonar_servo)
		time.sleep(0.5)
		self.servo.set_angle(self.servo_angle['center'])
		print("TO NO LEFT")
		##### If have way right, turn nose left ##
		if self.distance_dict['right'] > self.min_distance:
			for i in range(256):
				self.motor_1.motor_run(self.motor_1_pins,.001, 1,False, True,"half",0)
				self.motor_2.motor_run(self.motor_2_pins,.001, 1,False, True,"half",0)
			self.last_direction = 'left'
			self.direction = 'center'
		else:
			self.last_direction='left'
			self.direction = 'backward'


	def move_backward(self):
		## Moves both motor backward half turn ##
		print("Moving backward")
		for i in range(512):
			self.motor_1.motor_run(self.motor_1_pins,.001, 1,False,False,"half",0)
			self.motor_2.motor_run(self.motor_2_pins,.001, 1,True,False,"half",0)
			self.direction = self.last_direction


		
		


	def stop_movement(self):

		print("Stopped movement, starting Servo Checking")

		self.distance_dict = {'right':None,'center':None,'left':None} ## Clean Distance Dict
		##### Checking Servo ####
		#####  Looks right  #####
		#time.sleep(0.5)
		self.servo.set_angle(self.servo_angle['right'])
		time.sleep(0.5)
		self.distance_dict['right'] = self.sonar_mean(self.sonar_servo) ## Get Distance Right
		print("Distance Right: ", self.distance_dict['right'])
		time.sleep(0.5)

		########################
		#####  Looks Left  #####
		self.servo.set_angle(self.servo_angle['left'])
		time.sleep(0.5)
		self.distance_dict['left'] = self.sonar_mean(self.sonar_servo) ## Get Distance Left
		print("Distance Left:", self.distance_dict['left'])
		time.sleep(0.5)

		#######################
		##### Looks Foward ####
		self.servo.set_angle(self.servo_angle['center'])
		time.sleep(0.5)
		self.distance_dict['center'] = self.sonar_mean(self.sonar_servo) ## Get Foward distance
		print("Center Distance:", self.distance_dict['center'])

		max_value = max(self.distance_dict.values())
		## Check value key in dict to return
		for key, value in self.distance_dict.items():
			if value == max_value:
				side = key


		print("Max distance is to",side,",value:", max(self.distance_dict.values()))
		self.distance = self.sonar_mean(self.sonar)

		if side != 'center':
			self.last_direction = side

		if self.distance_dict['center']>max_value and self.distance>max_value:
			return 'center'
		elif self.distance_dict['left'] <= 7 or self.distance_dict['right'] <= 7 or self.distance_dict['center'] <= 7:
			return 'backward'
		else:
			self.last_direction = side
			return side

	
