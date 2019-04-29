import re
import pyimgur
import picamera
from time import sleep
import RPi.GPIO as GPIO
from twilio.rest import Client

# define the GPIO port you will use for the door sensor
SENSOR = 18

# number of seconds to delay between text notification and snapshot
DELAY = 2

#setup GPIO using Broadcom SOC channel numbering
GPIO.setmode(GPIO.BCM)

# set to pull-up (normally closed position for a door sensor)
GPIO.setup(SENSOR, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# put your Twilio credentials here
ACCOUNT_SID = "AC13aa1cd1edf10d03e9ebcdcc62a7d2a4"
AUTH_TOKEN = "7d1f475b5b658c0cf1a092ef2cad0595"

# make sure to use format with +1 for USA #s. E.G +12463338910
TO_PHONE = "+18572349615"
FROM_PHONE = "+18572715252"

# text message to send with photo
TXT_MSG_OP = "Door open!"
TXT_MSG_CL = "Door closed!"

# imgur client setup
CLIENT_ID = "cf89a79eab3c776"

# name and dimentsions of snapshot image
IMG = "snap.jpg"
IMG_WIDTH = 800
IMG_HEIGHT = 600

# initalize the Twilio client
client = Client(ACCOUNT_SID, AUTH_TOKEN)

# initialize imgur client
im = pyimgur.Imgur(CLIENT_ID)
#image = im.get_image('')
camera = picamera.PiCamera()

try:
	# setup an indefinite loop that looks for the door sensor to be opened
	while True:

		GPIO.wait_for_edge(SENSOR, GPIO.RISING)
		print("Door open! Camera activated!!\n")
		sleep(DELAY)
		
		camera.rotation = 180
		camera.resolution = (IMG_WIDTH, IMG_HEIGHT)

		camera.start_preview()
		for i in range(5):
			sleep(DELAY) #gives camera time to get ready to take the shot
			camera.capture('/home/pi/Desktop/image%s.jpg' % i)

		uploaded_image = im.upload_image('/home/pi/Desktop/image%s.jpg' % i, title=TXT_MSG)
		client.messages.create(
			to=TO_PHONE,
			from_=FROM_PHONE,
			body=TXT_MSG_OP,
			media_url=uploaded_image.link,
		)
	
		GPIO.wait_for_edge(SENSOR, GPIO.FALLING)
		print("Door is closed!")
		client.messages.create(
			to=TO_PHONE,
			from_=FROM_PHONE,
			body=TXT_MSG_CL
                 		)
finally:
	GPIO.cleanup() # ensures a clean exit on CTRL + C