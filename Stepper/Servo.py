import RPi.GPIO as GPIO
import time


class Servo_Class:

	def __init__(self, pin):

		self.servo_pin = pin ## pin 13

		#Ajuste estes valores para obter o intervalo completo do movimento do servo
		self.deg_0_pulse   = 0.5 
		self.deg_180_pulse = 2.5
		self.f = 50.0


		#Iniciar o pino gpio
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.servo_pin,GPIO.OUT)
		self.pwm = GPIO.PWM(self.servo_pin,self.f)
		self.pwm.start(0)
 

 
		# Faca alguns calculos dos parametros da largura do pulso
		self.period = 1000/self.f
		self.k      = 100/self.period
		self.deg_0_duty = self.deg_0_pulse*self.k
		self.pulse_range = self.deg_180_pulse - self.deg_0_pulse
		self.duty_range = self.pulse_range * self.k
 

 
	def set_angle(self,angle):
	        duty = self.deg_0_duty + (float(angle)/180.0)* self.duty_range
	        self.pwm.ChangeDutyCycle(duty)

	def input_angle(self):
	 
		try:
		        while True:
		                angle = input ("Enter angle (0 a 180): ")
		                self.set_angle(angle)
		 
		finally:
		        print("cleaning up")
		        GPIO.cleanup()



