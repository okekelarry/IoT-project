# Raspberry Pi Home security camera with motion detection #

## Prerequisites ##

Raspberry Pi with a pi-zero camera module installed and tested running with rasbian OS installed on a 32gb micro SD card with expanded file system.

Side Note: older raspbian build or pi-zero camera module and images are either black or have problems update raspberry pi firmware using sudo apt-get update or optional raspi-update.

## Setup: ##

### Hardware: ###
* Raspberry pi 3
* Micro Sd card 32 GB
* Power supply cables
* Pi-zero camera
* Door motion detector
* Pi Cobbler
* Bread board
* Connecting wires
* Pi power cable

### Software: ###
- OS - Raspbian
- Python 2.7
- Imgur API - A restful API based on HTTP request and Jason responses. will do the same thing a web server will do
- Twilio API - Cloud communications platform for building SMS, Voice & Messaging applications

## setup camera: ##
- Run this command on terminal to enable pi camera and select interfacing option to access option:
  - sudo raspi-config
- Run the following command to verify pi camera is connected correctly:
  - raspistill -o cam_test.jpg
- Update rpi with this command
  - sudo rpi-update

## Execute: ##
./file_name.py

or 

python file_name.py

## To-Do ##

- [X] update Raspberry pi firmware
- [X] Set up project repository
- [ ] Build demo and finist before 4/28
- [ ] Make improvements and modifications
