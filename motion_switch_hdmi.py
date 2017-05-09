#!/usr/bin/python
 
# libraries Laden
import RPi.GPIO as GPIO
import time
import datetime
import subprocess # Verwendet um per shell HDMI ein und aus zu schalten
 
# Um die Pin Nummer anstatt der gpio BCM Nummer anzugeben, verwenden wir den boardmode 

GPIO.setmode(GPIO.BOARD)
 
# GPIO definieren, 7 da bei mir der Sensor auf Pin7 steckt
GPIO_PIR = 7
 

# print " Test Bewegungsmelder (mit CTRL-C verlassen)"

 
#  GPIO Pin als input definieren
GPIO.setup(GPIO_PIR,GPIO.IN)
 
Current  = 0
Previous = 0
 
try:
 
 #print "%s: Auf den Sensor warten ..." % datetime.datetime.now() 
 time.sleep(120) # 2 min Pause, 
 
 # Warten bis Sensor sich meldet
 while GPIO.input(GPIO_PIR)==1:
   Current_State  = 0
 
 print "%s: Fertig! nur es bewegt sich keiner..."  % datetime.datetime.now()
 
 # Schleife bis nimmermehr ctrl-c unterbricht
 while True :
 
   #Sensor auslesen
   Current = GPIO.input(GPIO_PIR)
 
   if Current==1 and Previous==0:
     #print " %s:Erwischt! du hast dich Bewegt!" % datetime.datetime.now() 
     # Kommando zum anschalten, Frambuffer erneuern
     subprocess.Popen('echo Monitor on | wall', shell=True)
     subprocess.Popen('/opt/vc/bin/tvservice -p', shell=True)
     subprocess.Popen('fbset -depth 8', shell=True)
     subprocess.Popen('fbset -depth 16', shell=True)
     subprocess.Popen('sudo /bin/chvt 6 && sudo /bin/chvt 7', shell=True)
     
     Previous=1
   elif Current==0 and Previous==1:
     #print " %s: Fertig! Wieder alles ruhig"  % datetime.datetime.now() 
     # Ausschalten des Monitors
     subprocess.Popen('echo Monitor off | wall', shell=True)
     subprocess.Popen('/opt/vc/bin/tvservice -o', shell=True)
     Previous=0
 
   time.sleep(5) # 5sec Pause nach schleife
 
except KeyboardInterrupt:
 #print "und tschuess"
 GPIO.cleanup() # Aufraeumen 