#!/usr/bin/python
# -*- coding:utf-8 -*-

import SH1106
import time
import config
import traceback
import subprocess
import socket
import fcntl
import struct

from PIL import Image,ImageDraw,ImageFont

def get_ip_address():
 ip_address = '';
 s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 s.connect(("8.8.8.8",80))
 ip_address = s.getsockname()[0]
 s.close()
 return ip_address

try:
    disp = SH1106.SH1106()
    disp.Init()
    disp.clear()
    image1 = Image.new('1', (disp.width, disp.height), "WHITE")
    draw = ImageDraw.Draw(image1)
    font16 = ImageFont.truetype('Font.ttf', 16)
    font13 = ImageFont.truetype('Font.ttf', 13)
    draw.line([(0,0),(127,0)], fill = 0)
    draw.line([(0,0),(0,63)], fill = 0)
    draw.line([(0,63),(127,63)], fill = 0)
    draw.line([(127,0),(127,63)], fill = 0)
    draw.text((0,8), '      DIYElectronics', font = font13, fill = 0)
    draw.text((0,32), u'   RPI OLED Display', font = font13, fill = 0)
    #image1=image1.rotate(0) 
    disp.ShowImage(disp.getbuffer(image1))
    time.sleep(2)
    Himage2 = Image.new('1', (disp.width, disp.height), 255)
    bmp = Image.open('pic.bmp')
    Himage2.paste(bmp, (0,0))	
    disp.ShowImage(disp.getbuffer(Himage2))
    time.sleep(2)
    disp.clear()
    image2 = Image.new('1', (disp.width, disp.height), "WHITE")
    draw2 = ImageDraw.Draw(image2)
    IPAddress = str(get_ip_address())
    draw2.text((0,0), IPAddress, font = font16, fill = 0)
    disp.ShowImage(disp.getbuffer(image2))

except IOError as e:
    print(e)
    
except KeyboardInterrupt:    
    print("ctrl + c:")
    epdconfig.module_exit()
    exit()
