from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import time


#Asks for the interval of text being sent
def askForInterval():
    i=''
    while type(i) is not float:
        try:
            i= float(input(f'{Fore.BLUE}Input the message interval (s): {Style.RESET_ALL}'))
        except:
            print(f'{Fore.BLUE}PLEASE INPUT A NUMBER{Style.RESET_ALL}')
    return i

#Starts up the whole program
def initialize():
    with open('art.txt','r') as art:
        for lines in art:
            print(f'{Fore.BLUE}{lines}{Style.RESET_ALL}')
    return askForInterval()
    
#Starts the countdown towards activation
def countdown():
    seconds=''
    while type(seconds) is not int:
        try:
            seconds= int(input(f'{Fore.BLUE}Input the countdown time: {Style.RESET_ALL}'))
        except:
            print(f'{Fore.BLUE}PLEASE INPUT A WHOLE NUMBER{Style.RESET_ALL}')

    for second in range(seconds,-1,-1):
        print(f'{Fore.BLUE}You have {second} seconds to position your cursor: {Style.RESET_ALL}')
        time.sleep(1)

