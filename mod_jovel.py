from time import sleep

def head(msg):
    print('-'*30)
    print(f'{msg:^30}')
    print('-'*30)

def readint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31mERROR! Use an integer number to choose.\033[m')
            sleep(1)
        else:
            return n

def readstr(msg): 
    while True:
        try:
            n = str(input(msg))
        except:
            print(f'\033[0;31mERROR! Use an letter to choose.\033[m')
            sleep(1)
        else:
            return n 


def menu1():
    m1 = ['PLAY','QUIT']
    head('TIC-TAC-TOE')
    for e, i in enumerate(m1):
        print(f'{e+1} - {i}')
    print('-'*30)
    c = readint('Let\'s play? Choose a number: ')
    return c

def menu2():
    m2 = ['1Player, 2Players']
    head('TIC-TAC-TOE')
    for e, i in enumerate(m2):
        print(f'{e+1} - {i}')
    print('-'*30)
    c = readint('How many players? ')
    return c
    
def menu1():
    m3 = ['3x3','4x4','5x5']
    head('TIC-TAC-TOE')
    for e, i in enumerate(m3):
        print(f'{e+1} - {i}')
    print('-'*30)
    c = readint('Wich board do you want to play? ')
    return c

def board():
    b = [[1,2,3],[4,5,6],[7,8,9]]
    for i in range(0,3):
        for j in b:
            for k in b[i]:
                print(k)
