import RPi.GPIO as GPIO
import time
import read_RPM
import threading
import setup_robo
import sys
import multiprocessing
#from Gyro_new import Gyro


#from mpu6050 import mpu6050

class Control_robo:

    def __init__(self, encoder_1, encoder_2, SAMPLE_TIME, motor_1, motor_2):

        self.encoder_1 = encoder_1 ## LEFT ENCODER
        self.encoder_2 = encoder_2 ## RIGHT ENCODER
        ### RPM DATA TO USE ON PID
        self.RPM_1 = 0
        self.RPM_2 = 0

        self.SAMPLE_TIME = SAMPLE_TIME
        self.motor_1 = motor_1  ##LEFT MOTOR
        self.motor_2 = motor_2  ##RIGHT MOTOR
        
        ## SETUP PWM
        self.p = GPIO.PWM(self.motor_1.enable, 1000)
        self.p2 = GPIO.PWM(self.motor_2.enable, 1000)
        self.p.start(25)
        self.p2.start(25)

        ## SETUP START DUTY VALUES
        self.duty_1_value = 15
        self.duty_2_value = 15

        self.TARGET = 80 # USE ONLY WITH PID ENCODER CONTROL
        
        self.select = 'p'

    #PID CONTROL FOR RPM ONLY
    def background(self):

        def run(self):
            print("Starting Thread 1")
            thread1 = threading.Thread(target = pid_control, args = (self,))
            thread1.daemon = True
            thread1.start()


        def pid_control(self):

            ### PID TARGET AND COEFFICIENTS
            #TARGET = 80
            #KP = 0.02
            #KD = 0.01
            #KI = 0.0001


            ## PID RPM DATA
            KP = 0.05
            KD = 0.03
            KI = 0.0005

            e1_prev_error = 0
            e2_prev_error = 0


            e1_sum_error = 0
            e2_sum_error = 0
            
            while True:
            
                RPM = self.encoder_1.RPM()
                RPM_2 = self.encoder_2.RPM()
                print("MOTOR 1 ={}".format(int(RPM+0.5)))
                print("MOTOR 2 ={}".format(int(RPM_2+0.5)))

                if RPM < 600:
                    e1_error = self.TARGET - RPM
                if RPM_2 < 600:
                    e2_error = self.TARGET - RPM_2


                ## Diferencial error - better with delta "e" than with previous "e"?
                e1_diff = (e1_error - e1_prev_error)
                e2_diff = (e2_error - e2_prev_error)

                ## SET DUTY CYCLE VALUES FOR MOTORS
                if self.select in ('w', 's', 't', 'y', 'h','l','m'):
                    self.duty_1_value = self.duty_1_value + (e1_error * KP) + (e1_diff * KD) + (e1_sum_error * KI)
                    self.duty_2_value = self.duty_2_value + (e2_error * KP) + (e2_diff * KD) + (e1_sum_error * KI)
                elif self.select in ('d', 'h', 'l', 'm'):
                    self.duty_1_value = self.duty_1_value + (e1_error * KP) + (e1_prev_error * KD) + (e1_sum_error * KI)
                elif self.select in ('a', 'h','l','m'):
                    self.duty_2_value = self.duty_2_value + (e2_error * KP) + (e2_prev_error * KD) + (e2_sum_error * KI)

                ## DISCARD DUTY OVER 100 OR LESS THAN 0
                self.duty_1_value = max(min(100,self.duty_1_value), 0)
                self.duty_2_value = max(min(100, self.duty_2_value), 0)

                print("DUTY VALUE: ", self.duty_1_value)
                print("DUTY VALUE 2: ", self.duty_2_value)

                ## CHANGE DUTY CYCLE VALUES
                self.p.ChangeDutyCycle(self.duty_1_value)
                self.p2.ChangeDutyCycle(self.duty_2_value)

                
                time.sleep(self.SAMPLE_TIME/5) ## change the frequency 

                
                ## SET PREVIOUS ERROR
                e1_prev_error = e1_error
                e2_prev_error = e2_error

                ### IF STOP DONT INCREASE ERROR
                ## INTEGRAL ERROR
                #if self.select != 'p':
                e1_sum_error += e1_error
                e2_sum_error += e2_error

                print("error: ", e1_error)
                print("error2: ", e2_error)
                print("error soma: ", e1_sum_error)
                print("erro soma 2: ", e2_sum_error)


        run(self)
 

    def set_speed(self, x):

        temp1 = 1
        self.select = x
        if x == 'r':
            print("run")
            if (temp1 == 1):
                ##LEFT MOTOR
                GPIO.output(self.motor_1.in1, GPIO.HIGH)
                GPIO.output(self.motor_1.in2, GPIO.LOW)
                ##RIGHT MOTOR
                GPIO.output(self.motor_2.in1, GPIO.HIGH)
                GPIO.output(self.motor_2.in2, GPIO.LOW)
                print("forward")

                x = 'z'
            else:
                ##LEFT MOTOR
                GPIO.output(self.motor_1.in1, GPIO.LOW)
                GPIO.output(self.motor_1.in2, GPIO.HIGH)
                ##RIGHT MOTOR
                GPIO.output(self.motor_2.in1, GPIO.LOW)
                GPIO.output(self.motor_2.in2, GPIO.HIGH)
                print("backward")
                temp1 = 0 
                x = 'z'


        elif x == 'p':
            print("stop")
            ##LEFT MOTOR
            GPIO.output(self.motor_1.in1, GPIO.LOW)
            GPIO.output(self.motor_1.in2, GPIO.LOW)
            ##RIGHT MOTOR
            GPIO.output(self.motor_2.in1, GPIO.LOW)
            GPIO.output(self.motor_2.in2, GPIO.LOW)
            self.duty_1_value = 15
            self.duty_2_value = 15
            self.select = 'p'
            x='z'

        elif x == 'w':
            #print("forward")
            #self.gyro.calibration()
            self.duty_1_value = self.duty_1_value 
            self.duty_2_value = self.duty_2_value 
            ##LEFT MOTOR
            GPIO.output(self.motor_1.in1, GPIO.HIGH)
            GPIO.output(self.motor_1.in2, GPIO.LOW)
            ##RIGHT MOTOR
            GPIO.output(self.motor_2.in1, GPIO.HIGH)
            GPIO.output(self.motor_2.in2, GPIO.LOW)

            temp1 = 1
            x = 'z'
            self.select = 'w'

        elif x == 's':
            print("backward")
            
            #self.gyro.calibration()
            self.duty_1_value = self.duty_1_value
            self.duty_2_value = self.duty_2_value 
          
            ##LEFT MOTOR
            GPIO.output(self.motor_1.in1, GPIO.LOW)
            GPIO.output(self.motor_1.in2, GPIO.HIGH)
            ##RIGHT MOTOR
            GPIO.output(self.motor_2.in1, GPIO.LOW)
            GPIO.output(self.motor_2.in2, GPIO.HIGH)
            temp1 = 0
            x = 's'
            self.select = 's'
            
        elif x == 'd':
            print("turn right")
            ##LEFT MOTOR
            GPIO.output(self.motor_1.in1, GPIO.HIGH)
            GPIO.output(self.motor_1.in2, GPIO.LOW)
            ##RIGHT MOTOR
            GPIO.output(self.motor_2.in1, GPIO.LOW)
            GPIO.output(self.motor_2.in2, GPIO.LOW)
            x='z'
            
        elif x == 'a':
            print("turn left")
            ##LEFT MOTOR
            GPIO.output(self.motor_1.in1, GPIO.LOW)
            GPIO.output(self.motor_1.in2, GPIO.LOW)
            ##RIGHT MOTOR
            GPIO.output(self.motor_2.in1, GPIO.HIGH)
            GPIO.output(self.motor_2.in2, GPIO.LOW)
            x='z'
        
        elif x == 'y':
            print("axis rotation right")
            ##LEFT MOTOR
            GPIO.output(self.motor_1.in1, GPIO.HIGH)
            GPIO.output(self.motor_1.in2, GPIO.LOW)
            ##RIGHT MOTOR
            GPIO.output(self.motor_2.in1, GPIO.LOW)
            GPIO.output(self.motor_2.in2, GPIO.HIGH)
        
        elif x == 't':
            print("axis rotation left")
            ##LEFT MOTOR
            GPIO.output(self.motor_1.in1, GPIO.LOW)
            GPIO.output(self.motor_1.in2, GPIO.HIGH)
            ##RIGHT MOTOR
            GPIO.output(self.motor_2.in1, GPIO.HIGH)
            GPIO.output(self.motor_2.in2, GPIO.LOW)
        
        elif x == 'l':
            print("low")
            #self.p.ChangeDutyCycle(25)
            #self.p2.ChangeDutyCycle(25)
            self.TARGET_1 = 80
            self.TARGET_2 = 80
            x = 'z'

        elif x == 'm':
            print("medium")
            #self.p.ChangeDutyCycle(50)
            #self.p2.ChangeDutyCycle(50)
            self.TARGET_1 = 200
            self.TARGET_2 = 200
            x = 'z'

        elif x == 'h':
            print("high")
            #self.p.ChangeDutyCycle(100)
            #self.p2.ChangeDutyCycle(100)
            self.TARGET_1 = 250
            self.TARGET_2 = 250
            x = 'z'
        else:
            print("<<<  wrong data  >>>")