#intialize the appropiate libraries
import gpiozero
import time

#Setting up the pin lines
irsensor = gpiozero.DigitalInputDevice(9)

#Infinite Loop
while True: 
	if irsensor.is_active == False:
		print("Wall Detected")			#White line  detected
	else: 
		print("No Wall Detected")	#Black Line detected
	time.sleep(0.001)	

