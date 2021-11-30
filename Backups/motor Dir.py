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


GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p=GPIO.PWM(en,25)

p.start(100)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("\n")   
x=0
y=0 
v=0
while(1):

    xd=db.child("movx").get()
    yd=db.child("movy").get()
	yd=db.child("vel").get()
    x = xd.val()
    y = yd.val()
  	v = vd.val()
    print(x,y)
	p.ChangeDutyCycle(v)
    p2.ChangeDutyCycle(v)

    if x==0 and y==1:
        print("Davant")
		
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
		
       
        

 
    elif x==0 and y==0:
        print("stop")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        
   
    elif x==0 and y==-1:
        print("Darrere")
		
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        

    elif x==-1 and y==0:
        print("Esquerra")
		
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        

  elif x==-1 and y==1:
        print("Davant esquerra")
		p.ChangeDutyCycle(v/2)
    	p2.ChangeDutyCycle(v)
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
       
  elif x==-1 and y==-1:
        print("Darrere esquerra")
		p.ChangeDutyCycle(v/2)
    	p2.ChangeDutyCycle(v)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
      
  elif x==1 and y==0:
        print("Dreta")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
       

  elif x==1 and y==1:
        print("Davant dreta")
		p.ChangeDutyCycle(v)
        p2.ChangeDutyCycle(v/2)
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
      
  elif x==1 and y==-1:
        print("Darrere dreta")
		p.ChangeDutyCycle(v)
    	p2.ChangeDutyCycle(v/2)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
      