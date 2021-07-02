import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50) # Pin 11, 50Hz

servo1.start(0)

def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(11, True)
    servo1.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(11, False)
    servo1.ChangeDutyCycle(0)


SetAngle(0) 
servo1.stop()
GPIO.cleanup()

