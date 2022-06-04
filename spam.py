#spam message test
import time
import pyautogui
import os


def title():
  print("""


     _____ _           _      _____                                           
    / ____| |         | |    / ____|                                          
   | |    | |__   __ _| |_  | (___  _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
   | |    | '_ \ / _` | __|  \___ \| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
   | |____| | | | (_| | |_   ____) | |_) | (_| | | | | | | | | | | |  __/ |   
    \_____|_| |_|\__,_|\__| |_____/| .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
                                   | |                                        
                                   |_|                                        
      made by @ghatzz

  """)


def mainapp():
  inputf = input("Enter the message: ")
  times = int(input("How many times?: "))
  print("Sending messages...")
  time.sleep(2)
  for i in range(0,times):
    pyautogui.typewrite(inputf + '\n')
  time.sleep(1)
  print("Done")
  time.sleep(2)
  print("Quitting...")
  quit()


title()
time.sleep(2)
os.system('cls')
mainapp()
