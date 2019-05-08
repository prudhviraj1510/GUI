from tkinter import *
#import tkFont
import RPi.GPIO as GPIO
#import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.output(15, GPIO.LOW)
GPIO.output(16, GPIO.LOW)
GPIO.output(18, GPIO.LOW)
win = Tk()
#yFont = tkFont.Font(family = 'Helvitica', size = 36, weight = 'bold')
def led1():
    print ("LED button pressed")
    if GPIO.input(18):
        GPIO.output(18, GPIO.LOW)
        #ledButton["text"] = "LED ON"
    else:
        GPIO.output(18, GPIO.HIGH)
        #ledButton["text"] = "LED OFF"
def led2():
    print ("LED button pressed")
    if GPIO.input(16):
        GPIO.output(16, GPIO.LOW)
        #ledButton["text"] = "LED ON"
    else:
        GPIO.output(16, GPIO.HIGH)
        #ledButton["text"] = "LED OFF"
def led3():
    print ("LED button pressed")
    if GPIO.input(15):
        GPIO.output(15, GPIO.LOW)
        #ledButton["text"] = "LED ON"
    else:
        GPIO.output(15, GPIO.HIGH)
        #ledButton["text"] = "LED OFF"
def exitProgram():
    print("Exit Button Pressed")
    GPIO.cleanup()
    win.quit()
    
win.title("First GUI")
#win.geometry('800*480')

exitButton = Button(win, text = "EXIT",  command = exitProgram, height = 2, width =  8)
exitButton.pack(side = BOTTOM)

ledButton = Button(win, text = "LED 1",  command = led1, height = 2, width =  8)
ledButton.pack()
ledButton = Button(win, text = "LED 2",  command = led2, height = 2, width =  8)
ledButton.pack()
ledButton = Button(win, text = "LED 3",  command = led3, height = 2, width =  8)
ledButton.pack()
mainloop()


