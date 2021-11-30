from random import randint
from time import sleep
import mod_jovel 

def x3():
    l = [1,2,3,4,5,6,7,8,9]
    b = [[1,2,3],[4,5,6],[7,8,9]]
    return l,b

def board3(b):
    print()
    for i in range(0,3):
        for j in range(0,3):
            if (i,j) == (0,0) or (i,j) == (1,0) or (i,j) == (2,0):
                print(f' {b[i][j]}',end=' ')
            else:
                print(f'| {b[i][j]}',end=' ')
        print()
        if i == 2:
            print()
        else:
            print('-'*11)

def ctrl3(l,a=0):
    if a == 1:
        while True:
            n = randint(1,9)
            if n in l:
                break
    else:
        while True:
            n = mod_jovel.readint('Choose a number: ')
            if n in l:
                break
            else:
                if n in [1,2,3,4,5,6,7,8,9]:
                    print(f'\033[0;31mERROR! Number alredy choosen!\033[m')
                else:
                    print(f'\033[0;31mERROR! Choose only numbers between 1 and 9.\033[m')
    if n == 1:
        c = [0,0]
    elif n == 2:
        c = [0,1]
    elif n == 3:
        c = [0,2]
    elif n == 4:
        c = [1,0]
    elif n == 5:
        c = [1,1]
    elif n == 6:
        c = [1,2]
    elif n == 7:
        c = [2,0]
    elif n == 8:
        c = [2,1]
    elif n == 9:
        c = [2,2]
    return c, n

def wins3(b):
    if b[0][0] == b[0][1] == b[0][2]:
        w = True
    elif b[1][0] == b[1][1] == b[1][2]:
        w = True
    elif b[2][0] == b[2][1] == b[2][2]:
        w = True
    elif b[0][0] == b[1][0] == b[2][0]:
        w = True
    elif b[0][1] == b[1][1] == b[2][1]:
        w = True
    elif b[0][2] == b[1][2] == b[2][2]:
        w = True
    elif b[0][0] == b[1][1] == b[2][2]:
        w = True
    elif b[0][2] == b[1][1] == b[2][0]:
        w = True
    else:
        w = False
    return w

def game1p3():
    a = 'Y'
    while a == 'Y':
        while True:
            k1 = mod_jovel.readstr('Choose a symble: [O/X] ').strip().upper()[0]
            if k1 == 'O' or k1 == 'X':
                break
            else:
                print(f'\033[0;31mERROR! Choose only O or X.\033[m')
        if k1 == 'O':
            k2 = 'X'
        elif k1 == 'X':
            k2 = 'O'
        l,b = x3()
        while True:
            board3(b)
            print(f'Player {k1}')
            c,n = ctrl3(l)
            a = k1
            b = mod_jovel.changingb(c,b,a)
            l = mod_jovel.changingl(n,l)
            w = wins3(b)
            if w:
                break
            elif sum(l) == 0:
                break
            else:
                pass
            board3(b)
            print(f'Player {k2}')
            c,n = ctrl3(l,1)
            sleep(1)
            a = k2
            b = mod_jovel.changingb(c,b,a)
            l = mod_jovel.changingl(n,l)
            w = wins3(b)
            if w:
                break
            elif sum(l) == 0:
                break
            else:
                pass
        board3(b)
        if w:
            print(f'{a} wins')
        else: 
            print('Oh, we tied haha!')
        while True:
            a = mod_jovel.readstr('Do you want to play again? [Y/N] ').strip().upper()[0]
            if a == 'Y' or a == 'N':
                break
            else:
                print(f'\033[0;31mERROR! Choose only Y or N.\033[m')
    print('Finishing... Thanks for playing ;)')
    sleep(1)

def game2p3():
    a = 'Y'
    while a == 'Y':
        l,b = x3()
        while True:
            board3(b)
            print('Player O')
            c,n = ctrl3(l)
            a = 'O'
            b = mod_jovel.changingb(c,b,a)
            l = mod_jovel.changingl(n,l)
            w = wins3(b)
            if w:
                break
            elif sum(l) == 0:
                break
            else:
                pass
            board3(b)
            print('Player X')
            c,n = ctrl3(l)
            a = 'X'
            b = mod_jovel.changingb(c,b,a)
            l = mod_jovel.changingl(n,l)
            w = wins3(b)
            if w:
                break
            elif sum(l) == 0:
                break
            else:
                pass
        board3(b)
        if w:
            print(f'{a} wins')
        else: 
            print('Oh, we tied haha!')
        while True:
            a = mod_jovel.readstr('Do you want to play again? [Y/N] ').strip().upper()[0]
            if a == 'Y' or a == 'N':
                break
            else:
                print(f'\033[0;31mERROR! Choose only Y or N.\033[m')
    print('Finishing... Thanks for playing ;)')
    sleep(1)

game2p3()






