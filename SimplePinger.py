from pythonping import ping
import colorama
from colorama import init
from colorama import Fore, Back, Style
import time 
from time import sleep

print(Fore.LIGHTMAGENTA_EX + """   _____ _                 __     ____  _                      
  / ___/(_)___ ___  ____  / /__  / __ \(_)___  ____ ____  _____
  \__ \/ / __ `__ \/ __ \/ / _ \/ /_/ / / __ \/ __ `/ _ \/ ___/
 ___/ / / / / / / / /_/ / /  __/ ____/ / / / / /_/ /  __/ /    
/____/_/_/ /_/ /_/ .___/_/\___/_/   /_/_/ /_/\__, /\___/_/     
                /_/                         /____/             \n""")

snooze = input("Enter time between pings (0,1,2 [in s]): ")
address = input("Enter the IP Address you want to ping: ")
repeat = input("How many times do you want to ping the address?: ")

repeat = int(repeat)
snooze = int(snooze)

def pingit():
    for i in range(repeat):
        sleep(snooze)
        ping(f'{address}', verbose=True, size=472, count=1)

def done(): 
        print(Fore.WHITE + "Done, exiting in 3 seconds...")
        sleep(3)

pingit()
done()