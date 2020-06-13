import RPi.GPIO as GPIO
import time
import atexit


# Basic controls for a rapberry pi LED with safe power off
class PiLEDController():
		
	def __init__(self, LED):
		self.LED = LED
		self.startup()
		self.on = False
		atexit.register(self.cleanup)
	
	def poweron(self):
		if not self.on:
			GPIO.output(self.LED, True)
			self.on = True
		else:
			print("LED is already on!")
		
	def poweroff(self):
		if self.on:
			GPIO.output(self.LED, False)
			self.on = False
		else:
			print("LED is already off!")
	
	def startup(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.LED,GPIO.OUT)
		
	def cleanup(self):
		GPIO.cleanup()
		print("Successfully cleaned up LED ", self.LED)
