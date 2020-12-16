from random import randint, choice
import pyautogui
from time import sleep
import os
import subprocess
import time
from getmac import get_mac_address as gma
import socket    
   

def main():

    cmdAgain()
    print(gma())
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print(s.getsockname()[0])
    s.close()
    while 1:
        char1 = p.stdout.read(1)
        if char1 != b'':
            print(char1)
        if char1 == b'\x82' or char1 == "q" or b'\xe6':
            print("stop")
            moveMouse()
            #p.kill()
            time.sleep (6)
            cmdAgain()

def cmdAgain():
    global p
    cmd = ["sudo","nc", "-ul", "9"]
    p = subprocess.Popen(cmd,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)            
def moveMouse():
    sleep(1)
    pyautogui.moveTo(1000+randint(1,100), 950+randint(1,100),randint(20,100)/100)
    #pyautogui.moveTo(1020, 1035,1+randint(20,100)/100)
    pyautogui.moveTo(1020+randint(1,10), 1035+randint(1,10),randint(20,100)/100)
    pyautogui.click()
    
    

if __name__ == "__main__":
    main()
