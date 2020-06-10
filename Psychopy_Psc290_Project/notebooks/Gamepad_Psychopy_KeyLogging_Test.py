#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 22:36:05 2020

@author: desconcordia
"""
from pathlib import Path
from psychopy import visual, core
import Gamepad
import csv

if Gamepad.available():
    gamepad = Gamepad.Precision()
else:
    print('Controller not connected') 

path_parent = '/home/desconcordia/Documents/Psychopy_Psc290_Project/data' #had to hardcode bc running in anaconda env 
path = Path(path_parent)
data_log = 'Inputs_log.csv'
fpath = (path / data_log).with_suffix('.csv')


num_trials = 8 
button_press = []

win = visual.Window([400,400], color='black',colorSpace='rgb')

screen_text = visual.TextStim(win,text=None,
    alignHoriz="center", color = 'white')



for k in range(0,num_trials):
    
    eventType, control, value = gamepad.getNextEvent()

    if control == 'left': 
        button_press.append(1)
        print('left input successful')
        screen_text.setText('Wowwww you pressed the left key')
        screen_text.draw()
        win.flip()
        core.wait(2)
    elif control == 'right':
        button_press.append(0)
        print('right input successful')
        screen_text.setText('Wowwww you pressed the right key')
        screen_text.draw()
        win.flip()
        core.wait(2)
        
#Writing this all out to a CSV to be used for experiment.
with fpath.open(mode='w',newline='') as csvfile: 
    header = ['Left/Right Input']
    thewriter = csv.DictWriter(csvfile,fieldnames=header)
    thewriter.writeheader()
    for i in range(0,num_trials): 
        thewriter.writerow({'Left/Right Input':button_press[i]})


win.close()