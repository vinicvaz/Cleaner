import RPi.GPIO as GPIO
import time
from RpiMotorLib import RpiMotorLib
from Control import Control_Class
from Sonar import SonarClass
from Servo import Servo_Class
from server_SOCKET_TCP import Server_Socket
#from server_SOCKET_TCP import server_socket
import threading
import socket
import serial
import keyboard


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
servo = Servo_Class(13)

###### Setup Control #####
control = Control_Class(motor_1,motor_2,GPIO_PINS_1,GPIO_PINS_2,sonar, sonar_servo, servo)


##### Start Server on Backgroud thread #####
server = Server_Socket(control)
thread_teste = threading.Thread(target = server.handler)
thread_teste.daemon=True
thread_teste.start()



print("Press enter to start")

x = input()
if x=='':
	control.start_movement()

print("ERRO")




