#import librarie
import gpiozero
import time

#Attaching Constants
TRIG = 23
ECHO = 24

#Setting up pins to connect sensor
trigger = gpiozero.OutputDevice(TRIG)
echo	= gpiozero.DigitalInputDevice(ECHO)

#sending the signal 
trigger.on()
time.sleep(0.00001) #10 us
trigger.off()

while echo.is_active == False: 	#Missing the first echo signal recieve
	pulse_start = time.time()
while echo.is_active == True:	#Getting only the seond without noisy
	pulse_end = time.time()	
#calculate the pulse duration (difference pulse started - pulses ended)
pulse_duration = pulse_end - pulse_start # Do not get a negative value

#Calculating the distance 
distance = 34300*(pulse_duration/2)
round_distance = round(distance,1)

print("Distance is: ",round_distance)


