from random import randint
from time import sleep

def readstr(msg): 
    while True:
        n = input(msg)
        if not n.isalpha():
            print(f'\033[0;31mERROR! Use an letter to choose.\033[m')
            sleep(1)
        else:
            return n 

s = readstr('Escolhe algo: ')
print(s)





