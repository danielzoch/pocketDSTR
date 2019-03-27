# This file was made by Daniel Zoch and Daniyal Ansari for the Mobile Integrated Solutions Laboratory 
# at Texas A&M University. Special thanks to TStar and Matthew Leonard for the rights to the DSTR kit.
# This code was used to run a DSTR (Digital Systems Teaching & Research) robot using the Pocketbeagle.

import socket
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO

#        Define Server Properties

UDP_IP_ADDRESS = "192.168.1.1" # Use the same IP address from the Create_AP script
UDP_PORT_NO = 3553

#        GPIO Define pwms

pwm_l = "P2_1"  # GPIO050 (A PWM1) - Left Motors pwm
pwm_r = "P2_3"  # GPIO023 (B PWM2) - Right Motors pwm

digital_l = "P2_2"
digital_r = "P2_4"

DC_l = 0        # Duty Cycle in % from (0-100) - Left Motors pwm
DC_r = 0        # Duty Cycle in % from (0-100) - Right Motors pwm

#        Digital pwms Setup

GPIO.setup("P2_2", GPIO.OUT)
GPIO.setup("P2_4", GPIO.OUT)

#        Analog pwms Setup

PWM.start(pwm_l, 0, 1000)        # Start PWM on Left Motors pwm
PWM.start(pwm_r, 0, 1000)        # Start PWM on Right Motors pwm

#        UDP Server Setup

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

#        Loop

while 1:

    data = [187,254,187,254]

    data, addr = serverSock.recvfrom(1024)

    if data[0] == 170:
        DC_l = (data[3] / 2.55)
        GPIO.output(digital_l, GPIO.HIGH)

    if data[0] == 187:
        DC_l =  100 - (data[3] / 2.55)
        GPIO.output(digital_l, GPIO.LOW)

    if data[2] == 170:
        DC_r = (data[1] / 2.55)
        GPIO.output(digital_r, GPIO.HIGH)

    if data[2] == 187:
        DC_r = 100 - (data[1] / 2.55)
        GPIO.output(digital_r, GPIO.LOW)

    PWM.set_duty_cycle(pwm_l, DC_l)        # Set PWM on Left Motors pwm
    PWM.set_duty_cycle(pwm_r, DC_r)        # Set PWM on Right Motors pwm

    print(data[0],data[1],data[2],data[3], "\t", round(DC_l,1),"\t",round(DC_r,1))


PWM.stop(pwm_l)
PWM.stop(pwm_r)
PWM.cleanup()
    

