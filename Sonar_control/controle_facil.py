import RPi.GPIO as GPIO
import time
import read_RPM
import threading
import setup_robo
from Gyro_new import Gyro

class controle_facil():
	"""docstring for controle_facil"""
	def __init__(self,encoder_1,encoder_2,SAMPLE_TIME,motor_1,motor_2):
		self.encoder_1 = encoder_1
		self.encoder_2 = encoder_2
		self.SAMPLE_TIME = SAMPLE_TIME
		self.motor_1 = motor_1
		self.motor_2 = motor_2
		self.TARGET = 80 # USE ONLY WITH PID ENCODER CONTROL

	def set_Direction(self, string_opcao):
		temp1 = 1

		self.select = string_opcao

		if self.select == "stop":
			print("stop")
			##LEFT MOTOR
			GPIO.output(self.motor_1.in1, GPIO.LOW)
			GPIO.output(self.motor_1.in2, GPIO.LOW)
			##RIGHT MOTOR
			GPIO.output(self.motor_2.in1, GPIO.LOW)
			GPIO.output(self.motor_2.in2, GPIO.LOW)
			self.duty_1_value = 10
			self.duty_2_value = 10

		elif self.select == "forward":
			print("forward")
			##LEFT MOTOR
			GPIO.output(self.motor_1.in1, GPIO.HIGH)
			GPIO.output(self.motor_1.in2, GPIO.LOW)
			##RIGHT MOTOR
			GPIO.output(self.motor_2.in1, GPIO.HIGH)
			GPIO.output(self.motor_2.in2, GPIO.LOW)

		elif self.select == "backward":
			print("backward")
			##LEFT MOTOR
			GPIO.output(self.motor_1.in1, GPIO.LOW)
			GPIO.output(self.motor_1.in2, GPIO.HIGH)
			##RIGHT MOTOR
			GPIO.output(self.motor_2.in1, GPIO.LOW)
			GPIO.output(self.motor_2.in2, GPIO.HIGH)


		elif self.select == "right":
			print("axis rotation right")
			##LEFT MOTOR
			GPIO.output(self.motor_1.in1, GPIO.HIGH)
			GPIO.output(self.motor_1.in2, GPIO.LOW)
			##RIGHT MOTOR
			GPIO.output(self.motor_2.in1, GPIO.LOW)
			GPIO.output(self.motor_2.in2, GPIO.HIGH)

		elif x == "left":
			print("axis rotation left")
			##LEFT MOTOR
			GPIO.output(self.motor_1.in1, GPIO.LOW)
			GPIO.output(self.motor_1.in2, GPIO.HIGH)
			##RIGHT MOTOR
			GPIO.output(self.motor_2.in1, GPIO.HIGH)
			GPIO.output(self.motor_2.in2, GPIO.LOW)

		elif x == "low":
			print("low")
			self.TARGET = 80

		elif x == "medium":
			print("medium")
			self.TARGET = 200

		elif x == "high":
			print("high")
			self.TARGET = 300
		else:
			print("<<<  wrong data  >>>")