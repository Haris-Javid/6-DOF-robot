import RPi.GPIO as GPIO
import time


#servo specs; duty ratio = 0.5 ms - 2.5 ms, pluse period = 20 ms.

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

servo= GPIO.PWM(11,50)

servo.start(0)
print("waiting for 1 sec")
time.sleep(1);


duty=2

servo.ChangeDutyCycle(2.5);
time.sleep(1)
servo.ChangeDutyCycle(12.5);
time.sleep(1)

servo.stop()
GPIO.cleanup()


