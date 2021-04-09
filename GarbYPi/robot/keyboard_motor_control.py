#-------------------------------------------------------
#			    GarBy            		|
#		Semi-Autonomous Implementation		|
#	     		By Marcos Albetman       	|
#-------------------------------------------------------

#------------------- Import Libraries ------------------
import curses						#-> Support terminal-independent and keyboard handling facility for text based programs
import gpiozero						#-> Contain several types of interfaces for different electronic components
import time						#-> Varioud type of time based prebuilt functions
#-------------- Setting up Curses parameters -----------
screen = curses.initscr()				#-> Initialization of curses, this function return a window object representing the screen size
curses.noecho()						#-> To be able to read keyboard press and return their value onto the screen
curses.cbreak()						#-> React to sudden keyboard presses without pressing the enter button
screen.keypad(True)					#-> it can read and return spacial keys buttons
#--- Setting up Robot Class and Connections in Garby ---
robot = gpiozero.Robot(left=(17,18),right=(27,22))	#
#----------------------	 Main Body ---------------------
try:
	while True:					#-> Infinite loop
		char = screen.getch()			#-> Get a Charachter value from when Keyboard is pressed and stored in char
		if char == ord('q'):			#-> Quit the program when "Q" is pressed
			break				#
		elif char == curses.KEY_UP:		#-> Go forward when "Arrow up" key is pressed
			print "up"			#
			robot.forward(0.5)		#-> Robot moves 50% of Max Speed
			time.sleep(0.5)			#
		elif char == curses.KEY_DOWN:		#-> Go backwards when "Arrow Down" key is pressed
			print "down"			#
			robot.backward(0.5)		#
			time.sleep(0.5)			#
		elif char == curses.KEY_RIGHT:		#-> Go Right when "Arrow Right" key is pressed
			print "right"			#
			robot.right(0.5)		#
			time.sleep(0.5)			#
		elif char == curses.KEY_LEFT:		#-> Go Left when "Arrow Left" key is presssed
			print "left"
			robot.left(0.5)			#
			time.sleep(0.5)			#
		elif char == 10:			#
			print "stop"			#-> Stop when "Enter" key is pressed
			robot.stop()			#
			time.sleep(0.5)			#
finally:
	curses.nocbreak();screen.keypad(0);curses.echo() #-> Turn off all previous paramters from curses library
	curses.endwin()					 #-> Close windown and return to main terminal
