


import pyrebase
import time
import RPi.GPIO as GPIO

config = {
    "apiKey": "AIzaSyCd9OZrcaQZkKZuoNWyOEmnXI3MsXCzkvE",
    "authDomain": "produccio-multimedia-2.firebaseapp.com",
    "databaseURL": "https://produccio-multimedia-2.firebaseio.com",
    "storageBucket": "produccio-multimedia-2.appspot.com"
}


firebase = pyrebase.initialize_app(config)
db = firebase.database()

salida_luces=db.child("luces").get()
salida_message=db.child("message").get()




print "salida luces: ",salida_luces.val()
print "salida message: ", salida_message.val()



