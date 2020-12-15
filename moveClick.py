from random import randint, choice
import pyautogui
from time import sleep
import os
import subprocess
import time


def main():

    cmdAgain()
    while 1:
        print(p.stdout.read(1))
        if p.stdout.read(1) == b'\x82' or p.stdout.read(1) == "q":
            print("stop")
            moveMouse()
            p.kill()
            time.sleep (1)
            cmdAgain()

def cmdAgain():
    global p
    cmd = ["nc", "-ul", "9"]
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
