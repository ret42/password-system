import os
import requests
import time
import sys

if os.name == 'nt':
    os.system('title Password System Python')
else:
    sys.stdout.write("\x1b]2;Password System Python\x07")

pastebin = 'https://pastebin.com/raw/F8k39r74' #It can be github raw, ghostbin and other thing like that, just put the password into the raw.

Password = input('\033[1;31;40m[Password] >\033[0m ')
os.system('cls' if os.name == 'nt' else 'clear')

def begin():
  os.system('cls' if os.name == 'nt' else 'clear')
  print('\033[1;34;40mThank you for downloading my project.\033[0m')
  time.sleep(2)
  exit()

r = requests.get(pastebin).text

for line in r.split('\n'):
  if Password in line:
    print('\033[1;32;40mCorrect Password\033[0m')
    time.sleep(2)
    begin()
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\033[1;31;40mWrong Password, try again.\033[0m')
    time.sleep(2)
    exit()
