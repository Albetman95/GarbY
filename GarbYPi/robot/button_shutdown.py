import gpiozero
import time
import os

button = gpiozero.Button(21)
def Shutdown(channel):
	print("shutdown")
	time.sleep(5)
	os.system("sudo shutdown -h now")

while True:
	if button.is_pressed == True:
		print("button is pressed")
		shut = callback(Shutdown)
		while shut == True:
			time.sleep(1)
	else:
		print("button is not pressed")


