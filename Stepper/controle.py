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
		self.direction = 'n' ## w = foward, s=backward, d=right turn, l=left turn, p=stop, n=none
		###### Fix Values ######
		self.min_distance = 20
		



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
			self.direction = 'p'
			self.stop_movement()
		else:
			print("Starting movement Foward") ## Else start moving foward
			self.direction = 'w'
			self.move_foward()


	def move_foward(self):


		## Loops that checkes for servo and center sonar distances to keep going foward#
		while (self.distance > self.min_distance) and self.distance_dict['center'] > self.min_distance and (self.direction=='w'):

			self.distance = self.sonar.getDistance() ## Get Distance
			self.distance_dict['center'] = self.sonar_servo.getDistance()
			self.motor_1.motor_run(self.motor_1_pins,.001, 1,True,
		                  False,"half",0) ## 1 Step Foward for motor 1 
			self.motor_2.motor_run(self.motor_2_pins,.001, 1,False,
		                  False,"half",0) ## 1 step Foward for motor 2
		print("Stop foward mov with distance from object = ", self.distance)

		### Check Distances Mean ###
		self.distance_dict['center'] = self.sonar_mean(self.sonar_servo)
		self.distance = self.sonar_mean(self.sonar)

		if self.distance <= self.min_distance or self.distance_dict['center']<= self.min_distance:
			print("Minimun distance")
			self.direction = 'p'
			self.stop_movement()
		else:
			self.move_foward()
		
		


	def stop_movement(self):

		print("Stopped movement, starting Servo Checking")

		self.distance_dict = {'right':None,'center':None,'left':None} ## Clean Distance Dict
		##### Checking Servo ####
		#####  Looks right  #####
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
		time.sleep(0.5)


		print("Maior distancia = ", max(self.distance_dict.values()))




		














	'''
	def move_backwar(self):

	def turn_right(self):

	def turn left(self):

	def stop_movement(self);
	'''


