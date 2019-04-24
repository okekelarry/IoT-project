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

### Software: ###
- update pi using get-apt update
- Python 2.7
- Imgur API - A restful API based on HTTP request and Jason responses

## setup camera: ##
- sudo apt-get install python-picamera
- sudo apt-get install python3-picamera  # if running under python3

## Execute: ##
./file_name.py

or 

python file_name.py

## To-Do ##

- [X] update Raspberry pi firmware
- [X] Set up project repository
- [X] Build demo and finist before 4/28
- [ ] Make improvements and modifications
