import os
import time

def closing(websites,t):
  os.system(websites)
  time.sleep(t)
  os.system("TASKKILL /IM chrome.exe /F")

if __name__ == '__main__':
    websites=input("Enter website:")
    time_str=int(input("Enter Time in millisecons"))
    closing(websites,time_str)
