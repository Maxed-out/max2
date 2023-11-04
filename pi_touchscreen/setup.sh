

git clone https://github.com/ronberenstein/TouchScreenRelayPanel.git

sudo pip3 install guizero

# add these too
# from guizero import App, PushButton, Slider, Text
# from PIL import Image
# import rpi_backlight as bl
# import RPi.GPIO as GPIO

sudo crontab -e

@reboot python3 /home/pi/Desktop/main.py &