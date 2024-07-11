from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import time


#Asks for the interval of text being sent
def askForInterval():
    i=''
    while type(i) is not float:
        try:
            i= float(input('Input the message interval (s): '))
        except:
            print(f'PLEASE INPUT A NUMBER')
    return i

#Starts up the whole program
def initialize():
    with open('art.txt','r') as art:
        for lines in art:
            print(lines)
    return askForInterval()
    
#Starts the countdown towards activation
def countdown():
    seconds=''
    while type(seconds) is not int:
        try:
            seconds= int(input('Input the countdown time: '))
        except:
            print(f'PLEASE INPUT A WHOLE NUMBER')

    for second in range(seconds,-1,-1):
        print(f'You have {second} seconds to position your cursor:')
        time.sleep(1)

