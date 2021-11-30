import pyrebase
import RPi.GPIO as GPIO          
from time import sleep
import time
import datetime
config = {
    "apiKey": "AIzaSyCd9OZrcaQZkKZuoNWyOEmnXI3MsXCzkvE",
    "authDomain": "produccio-multimedia-2.firebaseapp.com",
    "databaseURL": "https://produccio-multimedia-2.firebaseio.com",
    "storageBucket": "produccio-multimedia-2.appspot.com"
}

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)

firebase = pyrebase.initialize_app(config)
db = firebase.database()
pr=0





trobat=0;
def func():
	dat=db.child("robot").child("numserie").child("77set").child("event").get()
	data=db.child("robot").child("numserie").child("77set").child("event").shallow().get()
	key=data.val()
	for i in key:


		any = db.child("robot").child("numserie").child("77set").child("event").child(i).child("temps").child("any").get()
		dia = db.child("robot").child("numserie").child("77set").child("event").child(i).child("temps").child("dia").get()
		hora = db.child("robot").child("numserie").child("77set").child("event").child(i).child("temps").child("hora").get()
		mes = db.child("robot").child("numserie").child("77set").child("event").child(i).child("temps").child("mes").get()
		minut = db.child("robot").child("numserie").child("77set").child("event").child(i).child("temps").child("minut").get()
		print(i)
			
	#print(any.val()) 
	#print(dia.val())
	#print(hora.val())
	#print(mes.val())
	#print(minut.val()) 
	
		anyK = any.val()
		diaK = dia.val()
		horaK = hora.val()
		mesK = mes.val()
		minutK = minut.val()
		minuminus = minutK - 5
		minumas = minutK + 5
		alert=0;
		if anyK == year and diaK == day and horaK == hour  and mesK == month :
			#print ("a")
			#print(minuminus)
			#print(minute)
			#print(minumas)
			entrada = 1
			if  minuminus < minute or minumas > minute :
				trobat = 1;
			else:
				trobat = 0;
		else:
			entrada= 0;
	
		if entrada == 1 and trobat == 1:
			alert = 1
		if alert == 0:
			GPIO.output(40, False)
		if alert == 1:
			GPIO.output(40, True)
			time.sleep(20)
			alert = 0



	#data=dat.val()
	#for robot in dat.each():
#key = dat.key();
#print(key)
	#hora = db.child(key).child("temps").get("hora")
	#print(dat)
	#print(data)
	#return data



nexttime = time.time()
while True:
	times = datetime.datetime.now()
#times = datetime.datetime(2020,12,30,11,22,00)

	year = times.strftime("%Y")
	month = times.strftime("%m")
	day = times.strftime("%d")
	hour = times.strftime("%H")
	minute = times.strftime("%M")

	print("Dia Actual "+day+"/"+month+"/"+year+"  "+hour+":"+minute)
	year = int(year)
	month = int(month)
	day = int(day)
	hour = int(hour)
	minute = int(minute)
	print(minute)
	func()
	#print("EL valor es" func())        
	nexttime += 10
	sleeptime = nexttime - time.time()
	if sleeptime > 0:
		time.sleep(sleeptime)
       
        