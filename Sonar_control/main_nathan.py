import RPi.GPIO as GPIO
import time
import read_RPM
from setup_robo import *
from controle_facil import *
import pigpio
import threading
import sys
from Sonar import *

##PINS
temp1 = 1
####################
##SETUP RPM MEASURING
RPM_GPIO = 4
RPM_GPIO_2 = 17
RUN_TIME = 60.0
SAMPLE_TIME = 2.0

pi = pigpio.pi()
pi2 = pigpio.pi()
###################

##SETUP ENCODERS
encoder_1 = read_RPM.reader(pi, RPM_GPIO)
encoder_2 = read_RPM.reader(pi2, RPM_GPIO_2)
###################

### SETUP MOTORS BCM PINS (EN, IN1, IN2) ###
motor_1 = Setup_robo(25,24,23)
motor_1.set_motors()
#### SET MOTOR 2 ###
motor_2 = Setup_robo(6,16,26)
motor_2.set_motors()
### SONAR ####
sonar = Sonar.Sonar(22,27) ## pinos gpio sonar
### CONTROLE ####
controle = controle_facil(encoder_1,encoder_2,SAMPLE_TIME,motor_1,motor_2)
#################

while True:
	distanciaCM = sonar.getDistance()
	if (distanciaCM < 40):
		controle.set_Direction("backward")
		time.sleep(2)
		controle.set_Direction("left")
	if (distanciaCM > 40 or distanciaCM < 2)
		controle.set_Direction("forward")