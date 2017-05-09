# IoTClass-SmartCam
This was my project for my SEIS 744 IoT class semester project. It takes a webcam connected to a raspberry pi and sends images to the server while comparing the new image to the old one to see if there is a percent difference between the two. If there is it will call and endpoint in the server side code to send an email.

# Build
First you will need tp put the .PY file on your raspberry pi. You can then run it from there manually or setup the script to run on boot.
You will need to load the .sln file in visual studio. Once you do that you will get a compiler error. If you follow the error it will take you to where you need to input you gmail email and password so that notifications can be sent.

# Hardware
You will need to have a webcam (USB or a PICam) connected to your raspberry pi. You will also need to setup your pi to connect to the internet (either ethernet cable or wireless).

# First Time Run
The first time you run the server side code you will get an error trying to send a notification for the first time. Shortly after you will get an email from google saying they blocked an insecure app from sending an email. There will be a link to allow insecure apps. Allow this for as long as you are using the code. Be sure to switch it back when you are done for good gmail security.

# My Hardware
Raspberry Pi2 running raspbian
Xbox 360 USB Vision cam,
raspberry pi starter kit WiFi USB adaptor,
USB powerbank

# Software
Pything IDE3 (came with raspbian),
Visual Studio 2017 Community
