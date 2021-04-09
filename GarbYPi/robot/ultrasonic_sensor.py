#import libraries
import gpiozero
import time

#Setting Pins Constant
TRIG = 23
ECHO = 24

#Setting in/out
trigger = gpiozero.OutputDevice(TRIG)
echo = gpiozero.DigitalInputDevice(ECHO)

#Creatting the function
def get_distance(trigger,echo):
	trigger.on()
	time.sleep(0.00001)
	trigger.off()

	while echo.is_active == False:
		pulse_start = time.time()
	while echo.is_active == True:
		pulse_end = time.time()
	pulse_duration = pulse_end - pulse_start
	distance = 34300*(pulse_duration/2)
	round_distance = round(distance,1)
	return(round_distance)

while True:
	dist = get_distance(trigger,echo)
	print(dist)
	time.sleep(0.001)

