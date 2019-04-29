# Raspberry Pi Home security camera with motion detection and sms alert #

## Prerequisites ##

Raspberry Pi with a pi-zero camera module installed and tested running with rasbian OS installed on a 32gb micro SD card with expanded file system.

Side Note: older raspbian build or pi-zero camera module and images are either black or have problems updating raspberry pi firmware using sudo apt-get update or optional raspi-update.

## Setup: ##

### Hardware: ###
* Raspberry pi 3
* Micro Sd card 32 GB
* Pi-zero camera
* Door motion detector
* Pi Cobbler
* Bread board
* Connecting wires
* Pi power cable

### Software: ###
- Raspbian - Operating system
- Python 2.7
- Imgur API - A restful API based on HTTP request and JSon request
  - Link to Imgur API [Imgur API](https://api.imgur.com/)
- Twilio API - Cloud communications platform for building SMS, Voice & Messaging applications
  - Link to Twilio API [Twilio API](https://www.twilio.com/docs/usage/api)
- picamera

## RPi.GPIO Setup ##
`$ pip install RPi.GPIO`

- For more info on RPi.GPIO [Click here!](https://pypi.org/project/RPi.GPIO/)

## setting up pyimgur ##
Github page to setup pyimgur and more [Click pyimgur!](https://github.com/Damgaard/PyImgur)

## setting up twilio ##
Setup page for Twilio-python and more [Click twilio!](https://www.twilio.com/docs/libraries/python)

## Twilio sms/picture send/recieve price table ##
Twilio sms/picture price table [Click twilio!](https://www.twilio.com/sms/pricing/us)


## setting up Python Picamera ##
Setup for python Picamera and more [Click python picamera!](https://picamera.readthedocs.io/en/release-1.0/install2.html)

## setup and test camera: ##
- Run this command on terminal to enable pi camera and select interfacing option to access option:
  - sudo raspi-config
- Run the following command to verify pi camera is connected correctly:
  - raspistill -o cam_test.jpg
- Update rpi with this command
  - sudo rpi-update

## Execute: ##
python sms-imgur-alert.py

## To-Do ##

- [X] update Raspberry pi firmware
- [X] Set up project repository
- [X] Build demo and finist before 4/29
- [X] Make improvements and finish project 4/29
