from random import randint, choice
import pyautogui
from time import sleep
import os


def main():

    pingAndroid()
    while 1:
        sleep(2)
        upOrDown = pingAndroid()
        if upOrDown =="down":
            moveMouse()
            sleep(30)
            
def moveMouse():
    sleep(1)
    pyautogui.moveTo(1000+randint(1,100), 950+randint(1,100),randint(20,100)/100)
    #pyautogui.moveTo(1020, 1035,1+randint(20,100)/100)
    pyautogui.moveTo(1020+randint(1,10), 1035+randint(1,10),randint(20,100)/100)
    pyautogui.click()
    
    
def pingAndroid():


    hostname = "192.168.0.25" #example
    response = os.system("timeout 4 ping -c 1 {}".format(hostname))

    #and then check the response...
    if response == 0:
        print(hostname, 'is up!')
        return "up"
    else:
        print(hostname, 'is down!')
        return "down"




if __name__ == "__main__":
    main()
