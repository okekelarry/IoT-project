from picamera import piCamera
from time import sleep

camera = piCamera()

camera.rotation = 180
camera.start_preview()
for i in range(5):
	sleep(5) #gives camera time to get ready to take the shot
	camera.capture('/home/pi/Desktop/image%s.jpg' % i)
camera.stop_preview()
