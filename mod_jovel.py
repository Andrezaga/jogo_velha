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
    
def menu3():
    m3 = ['3x3','4x4','5x5']
    head('TIC-TAC-TOE')
    for e, i in enumerate(m3):
        print(f'{e+1} - {i}')
    print('-'*30)
    c = readint('Wich board do you want to play? ')
    return c

def board3(b):
    print('-'*13)
    for i in b:
        for j in i:
            print(f'| {j}',end=' ')
        print('|')
        print('-'*13)

def board4(b):
    print('-'*25)
    for i in b:
        for j in i:
            print(f'| {j:^3}',end=' ')
        print('|')
        print('-'*25)

def board5(b):
    print('-'*31)
    for i in b:
        for j in i:
            print(f'| {j:^3}',end=' ')
        print('|')
        print('-'*31)
def x3():
    b = [[1,2,3],[4,5,6],[7,8,9]]
    return b

def x3():
    b = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    return b

def x3():
    b = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    return b

def ctrl():
    n = input('Choose a number: ')
    if n == 1:
        c = 0,0
    elif n == 2:
        c = 0,1
    elif n == 3:
        c = 0,2
    elif n == 4:
        c = 1,0
    elif n == 5:
        c = 1,1
    elif n == 6:
        c = 1,2
    elif n == 7:
        c = 2,0
    elif n == 8:
        c = 2,1
    elif n == 9:
        c = 2,2
    return c

def changing(c,b,k):
    b[c] = k




    
