#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 17:44:58 2020

@author: desconcordia
"""

import os 
from psychopy import visual, event, core 
import Gamepad

if Gamepad.available():
    gamepad = Gamepad.Precision()
else:
    print('Controller not connected') 
 

win = visual.Window(units = 'pix', color = 'black')

x = 0 
y = 0

LEFT = -100 
RIGHT = 100 

circle = visual.Circle(win, radius =10, fillColor = 'blue')

while True: 
    
    eventType, control, value = gamepad.getNextEvent()
    
    if control: 
        if 'left' in control:
            x = LEFT
        elif 'right' in control:
            x = RIGHT
        elif 'down' in control:
            core.quit()
            
    y += 10
    circle.pos = [x,y]
    circle.draw()
    win.flip()
win.close() 
core.quit()