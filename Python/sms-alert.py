import time
from camera import *
import picamera
import RPi.GPIO as GPIO
import twilio
from twilio.rest import TwilioRestClient

# define the GPIO port you will use for the door sensor
SENSOR = 19

# number of seconds to delay between alarm and snapshot
# in case you want to wait a second or two for the person to enter the room after triggering the sensor
DELAY = 0

#setup GPIO using Broadcom SOC channel numbering
GPIO.setmode(GPIO.BCM)

# set to pull-up (normally closed position for a door sensor)
GPIO.setup(SENSOR, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# put your Twilio credentials here
ACCOUNT_SID = "Yours"
AUTH_TOKEN = "Yours"

# make sure to use format with +1 for USA #s. E.G +12463338910
TO_PHONE = "+185727152**" #Twilio generated phone number for communicating with my phone
FROM_PHONE = ""

# text message to send with photo
TXT_MSG = "Door Opened!"

# hostname or IP address of Raspberry Pi + port number
HOSTNAME = "Yours"

# name and dimensions of snapshot image
IMG = "snap.jpg"
IMG_WIDTH = 800
IMG_HEIGHT = 600

# initalize the Twilio client
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

try:
        # setup an indefinite loop that looks for the door sensor to be opened
        while True:

                GPIO.wait_for_edge(SENSOR, GPIO.RISING)
                print("Door Opened!\n")
                time.sleep(DELAY)
                with picamera.PiCamera() as camera:
                        camera.resolution = (IMG_WIDTH, IMG_HEIGHT)
                        camera.capture(APACHE_DOC_ROOT + IMG)

                client.messages.create(
                        to=TO_PHONE,
                        from_=FROM_PHONE,
                        body=TXT_MSG,
                        media_url="http://" + HOSTNAME + "/" + IMG,
                )
finally:
        GPIO.cleanup() # ensures a clean exit

