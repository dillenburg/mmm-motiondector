#!/usr/bin/python
 
# libraries Laden
import RPi.GPIO as GPIO
import time
import datetime
 
# Um die Pin Nummer anstatt der gpio BCM Nummer anzugeben, verwenden wir den boardmode 

GPIO.setmode(GPIO.BOARD)
 
# GPIO definieren, 7 da bei mir der Sensor auf Pin7 steckt
GPIO_PIR = 7
 

print " Test Bewegungsmelder (mit CTRL-C verlassen)"

 
#  GPIO Pin als input definieren
GPIO.setup(GPIO_PIR,GPIO.IN)
 
Current  = 0
Previous = 0
 
try:
 
 print "%s: Auf den Sensor warten ..." % datetime.datetime.now() 
 
 # Warten bis Sensor sich meldet
 while GPIO.input(GPIO_PIR)==1:
   Current_State  = 0
 
 print "%s: Fertig! nur es bewegt sich keiner..."  % datetime.datetime.now()
 
 # Schleife bis nimmermehr ctrl-c unterbricht
 while True :
 
   #Sensor auslesen
   Current = GPIO.input(GPIO_PIR)
 
   if Current==1 and Previous==0:
     print " %s:Erwischt! du hast dich Bewegt!" % datetime.datetime.now() 
     Previous=1
   elif Current==0 and Previous==1:
     print " %s: Fertig! Wieder alles ruhig"  % datetime.datetime.now() 
     Previous=0
 
   time.sleep(0.01)
 
except KeyboardInterrupt:
 print "und tschuess"
 GPIO.cleanup() # Aufraeumen 
