from random import randint
from time import sleep

def ctrl5(l,a=0):
    if a == 1:
        while True:
            n = randint(1,25)
            if n in l:
                break
    else:
        while True:
            n = int(input('Choose a number: '))
            if n in l:
                break
            else:
                print('ERROR! Number alredy choosen!')
    if n == 1:
        c = [0,0]
    elif n == 2:
        c = [0,1]
    elif n == 3:
        c = [0,2]
    elif n == 4:
        c = [0,3]
    elif n == 5:
        c = [0,4]
    elif n == 6:
        c = [1,0] 
    elif n == 7:
        c = [1,1]
    elif n == 8:
        c = [1,2]
    elif n == 9:
        c = [1,3]
    elif n == 10:
        c = [1,4]
    elif n == 11:
        c = [2,0]
    elif n == 12:
        c = [2,1]
    elif n == 13:
        c = [2,2]
    elif n == 14:
        c = [2,3]
    elif n == 15:
        c = [2,4]
    elif n == 16:
        c = [3,0]
    elif n == 17:
        c = [3,1]
    elif n == 18:
        c = [3,2]
    elif n == 19:
        c = [3,3]
    elif n == 20:
        c = [3,4]
    elif n == 21:
        c = [4,0]
    elif n == 22:
        c = [4,1]
    elif n == 23:
        c = [4,2]
    elif n == 24:
        c = [4,3]
    elif n == 25:
        c = [4,4]

    else:
        print('Choose an integer number')
    return c, n

def changingb(c,b,k):
    b[c[0]][c[1]] = k
    return b

def changingl(n,l):
    l[n-1] = 0
    return l

def x5():
    l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    b = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    return l,b

def board5(b):
    print('-'*31)
    for i in b:
        for j in i:
            print(f'| {j:^3}',end=' ')
        print('|')
        print('-'*31)

def wins5(b):
    if b[0][0] == b[0][1] == b[0][2] == b[0][3] == b[0][4]:
        w = True
    elif b[1][0] == b[1][1] == b[1][2] == b[1][3] == b[1][4]:
        w = True
    elif b[2][0] == b[2][1] == b[2][2] == b[2][3] == b[2][4]:
        w = True
    elif b[3][0] == b[3][1] == b[3][2] == b[3][3] == b[3][4]:
        w = True
    elif b[3][0] == b[3][1] == b[3][2] == b[3][3] == b[4][4]:
        w = True
    elif b[0][0] == b[1][0] == b[2][0] == b[3][0] == b[4][0]:
        w = True
    elif b[0][1] == b[1][1] == b[2][1] == b[3][1] == b[4][1]:
        w = True
    elif b[0][2] == b[1][2] == b[2][2] == b[3][2] == b[4][2]:
        w = True
    elif b[0][3] == b[1][3] == b[2][3] == b[3][3] == b[4][3]:
        w = True
    elif b[0][4] == b[1][4] == b[2][4] == b[3][4] == b[4][4]:
        w = True
    elif b[0][0] == b[1][1] == b[2][2] == b[3][3] == b[4][4]:
        w = True
    elif b[0][4] == b[1][3] == b[2][2] == b[3][1] == b[4][0]:
        w = True
    else:
        w = False
    return w
    
def game1p5():
    a = 'Y'
    while a == 'Y':
        k1 = input('Choose a symble: [O/X] ').strip().upper()[0]
        if k1 == 'O':
            k2 = 'X'
        elif k1 == 'X':
            k2 = 'O'
        l,b = x5()
        while True:
            board5(b)
            print(f'Player {k1}')
            c,n = ctrl5(l)
            a = k1
            b = changingb(c,b,a)
            l = changingl(n,l)
            w = wins5(b)
            if w:
                break
            else:
                pass
            board5(b)
            print(f'Player {k2}')
            c,n = ctrl5(l,1)
            sleep(1)
            a = k2
            b = changingb(c,b,a)
            l = changingl(n,l)
            w = wins5(b)
            if w:
                break
            else:
                pass
        board5(b)
        print(f'{a} wins')
        a = input('Do you want to play again? [Y/N] ').strip().upper()[0]
    print('Finishing... Thanks for playing ;)')

def game2p5():
    a = 'Y'
    while a == 'Y':
        l,b = x5()
        while True:
            board5(b)
            print('Player O')
            c,n = ctrl5(l)
            a = 'O'
            b = changingb(c,b,a)
            l = changingl(n,l)
            w = wins5(b)
            if w:
                break
            else:
                pass
            board5(b)
            print('Player X')
            c,n = ctrl5(l)
            a = 'X'
            b = changingb(c,b,a)
            l = changingl(n,l)
            w = wins5(b)
            if w:
                break
            else:
                pass
        board5(b)
        print(f'{a} wins')
        a = input('Do you want to play again? [Y/N] ').strip().upper()[0]
    print('Finishing... Thanks for playing ;)')

game2p5()




