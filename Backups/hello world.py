import RPi.GPIO as GPIO
import time
pin = 7
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin,GPIO.OUT)


while True:
	GPIO.output(pin,GPIO.HIGH)
	print("HelloWord")
	time.sleep(1)
	GPIO.output(pin,GPIO.LOW)
	time.sleep(1)

GPIO.cleanup() 
