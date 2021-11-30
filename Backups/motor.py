
import pyrebase
import RPi.GPIO as GPIO          
from time import sleep

config = {
    "apiKey": "AIzaSyCd9OZrcaQZkKZuoNWyOEmnXI3MsXCzkvE",
    "authDomain": "produccio-multimedia-2.firebaseapp.com",
    "databaseURL": "https://produccio-multimedia-2.firebaseio.com",
    "storageBucket": "produccio-multimedia-2.appspot.com"
}


firebase = pyrebase.initialize_app(config)
db = firebase.database()



in1 = 24
in2 = 23
en = 25
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p=GPIO.PWM(en,1000)

p.start(75)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

while(1):

    x=db.child("message").get()


    
    if x.val()=='r':
        print("forward")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        temp1=1
        x='z'

    elif x.val()=='b':
        print("backward")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        temp1=0
        x='z'

  
    elif x.val()=='e':
        GPIO.cleanup()
        print("GPIO Clean up")
        break
    
   