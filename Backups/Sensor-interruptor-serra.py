import RPi.GPIO as GPIO    
import time               
GPIO.setmode(GPIO.BCM)
in1 = 23
in2 = 24
en = 25

in3 = 7
in4 = 8
en2 = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
GPIO.setup(en2,GPIO.OUT)
GPIO.setup(2, GPIO.IN)
GPIO.setup(3, GPIO.IN)
p=GPIO.PWM(en,1000)
p2=GPIO.PWM(en2,1000)
p.start(100)
p2.start(100)






#Usamos el pin GPIO 24 como TRIGGER
trigger = 4
#Usamos el pin GPIO 23 como ECHO
echo = 17    
GPIO.setup(trigger,GPIO.OUT)  #Configuramos Trigger como salida
GPIO.setup(echo,GPIO.IN)      #Configuramos Echo como entrada

GPIO.output(trigger,GPIO.LOW)    #Ponemos el pin 25 como LOW

def lecturaDistancia():
    #Enviamos un pulso de ultrasonidos duntate un corto tiempo
    GPIO.output(trigger,GPIO.HIGH)
    time.sleep(0.00001)              
    GPIO.output(trigger,GPIO.LOW)
    #Mientras el sensor no reciba señal el eco
    while GPIO.input(echo)==0:  
        #Guardamos el inicio del intervalo
        inicio = time.time()
    #Mientras en sensor reciba el eco
    while GPIO.input(echo)==1:
        #Guardamos el fin del intervalo
        fin = time.time()
        #intervalo entre envío y recepción
    intervalo = float(fin-inicio)             
    #Distancia es igual a tiempo por velocidad del sonido dividido por dos:
    #la ida y la vuelta
    distancia = float((intervalo * 34320)/2)
    #Con la formula del fabricante sería:
    #distancia = float(intervalo / 0.000058 ) #para cm
    #distancia = float(intervalo / 0.000148 ) #para pulgadas
    return distancia
  	  
lecturas=float(10.00)
try:
	while True:
		dist=lecturaDistancia()
		print ("Measured Distance = %f cm" % dist)
		time.sleep(1)
		if GPIO.input(2):
			print("MODO BATALLA")
			if dist<lecturas:
				GPIO.output(in1,True)
				GPIO.output(in2,False)
			else:
				GPIO.output(in1,GPIO.LOW)
				GPIO.output(in2,GPIO.LOW)
				
		if GPIO.input(3):
			print("MODO CASA")
			GPIO.output(in1,GPIO.LOW)
			GPIO.output(in2,GPIO.LOW)
			
			
except KeyboardInterrupt:  
	print("Measurement stopped by User")
	GPIO.cleanup()