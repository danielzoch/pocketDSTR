# This script tests PWMs for the Pocketbeagle. Special thanks to Daniyal Ansari and Daniel Zoch in
# conjunction with the Mobile Integrated Solutions Laboratory at Texas A&M University.


import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO

pwm_l = "P2_1"          # GPIO050 (A PWM1) - Left Motors Pin
pwm_r = "P2_3"          # GPIO050 (A PWM1) - Left Motors Pin

dig_l = "P2_2"
dig_r = "P2_4"

DC = 0  # Duty Cycle in % from (0-100) - Left Motors Pin

PWM.start(pwm_l, 0, 1000)       # Start PWM on Left Motors Pin
PWM.start(pwm_r, 0, 1000)       # Start PWM on Left Motors Pin

GPIO.setup(dig_l, GPIO.OUT)
GPIO.setup(dig_r, GPIO.OUT)

while 1:

    PWM.set_duty_cycle(pwm_l, DC)       # Set PWM on Left Motors Pin
    GPIO.output(dig_l, GPIO.LOW)
    PWM.set_duty_cycle(pwm_r, DC)       # Set PWM on Left Motors Pin
    GPIO.output(dig_r, GPIO.LOW)

PWM.stop(pin)
PWM.cleanup()
