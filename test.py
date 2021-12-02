from random import randint 
from time import sleep 
import mod_jovel 

def x5():
    l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    b = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    return l,b

def board5(b):
    print(f'{"Quit[0]":>38}')
    for i in range(0,5):
        for j in range(0,5):
            if b[i][j] == 'X' or b[i][j] == 'O':
                if (i,j) == (0,0) or (i,j) == (1,0) or (i,j) == (2,0):
                    print(f' \033[0;33m{b[i][j]:^3}\033[m',end=' ')
                else:
                    print(f'| \033[0;33m{b[i][j]:^3}\033[m',end=' ')
            else:
                if (i,j) == (0,0) or (i,j) == (1,0) or (i,j) == (2,0) or (i,j) == (3,0) or (i,j) == (4,0):
                    print(f' {b[i][j]:^3}',end=' ')
                else:
                    print(f'| {b[i][j]:^3}',end=' ')
        print()
        if i == 4:
            print()
        else:
            print('-'*29)

def ctrl5(l,a=0):
    if a == 1:
        while True:
            n = randint(1,25)
            if n in l:
                break
    else:
        while True:
            n = mod_jovel.readint('Choose a number: ')
            if n in l:
                break
            if n == 0:
                break
            else:
                if n in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]:
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
        c = 0
    return c, n

def wins5(b):
    if b[0][0] == b[0][1] == b[0][2]:
        w = True
    elif b[0][1] == b[0][2] == b[0][3]:
        w = True
    elif b[0][2] == b[0][3] == b[0][4]:
        w = True
    elif b[1][0] == b[1][1] == b[1][2]:
        w = True
    elif b[1][1] == b[1][2] == b[1][3]:
        w = True
    elif b[1][2] == b[1][3] == b[1][4]:
        w = True
    elif b[2][0] == b[2][1] == b[2][2]:
        w = True
    elif b[2][1] == b[2][2] == b[2][3]:
        w = True
    elif b[2][2] == b[2][3] == b[2][4]:
        w = True
    elif b[3][0] == b[3][1] == b[3][2]:
        w = True
    elif b[3][1] == b[3][2] == b[3][3]:
        w = True
    elif b[3][2] == b[3][3] == b[3][4]:
        w = True
    elif b[4][0] == b[4][1] == b[4][2]:
        w = True
    elif b[4][1] == b[4][2] == b[4][3]:
        w = True
    elif b[4][2] == b[4][3] == b[4][4]:
        w = True
    elif b[0][0] == b[1][0] == b[2][0]:
        w = True
    elif b[1][0] == b[2][0] == b[3][0]:
        w = True
    elif b[2][0] == b[3][0] == b[4][0]:
        w = True
    elif b[0][1] == b[1][1] == b[2][1]:
        w = True
    elif b[1][1] == b[2][1] == b[3][1]:
        w = True
    elif b[2][1] == b[3][1] == b[4][1]:
        w = True
    elif b[0][2] == b[1][2] == b[2][2]:
        w = True
    elif b[1][2] == b[2][2] == b[3][2]:
        w = True
    elif b[2][2] == b[3][2] == b[4][2]:
        w = True
    elif b[0][3] == b[1][3] == b[2][3]:
        w = True
    elif b[1][3] == b[2][3] == b[3][3]:
        w = True
    elif b[2][3] == b[3][3] == b[4][3]:
        w = True
    elif b[0][4] == b[1][4] == b[2][4]:
        w = True
    elif b[1][4] == b[2][4] == b[3][4]:
        w = True
    elif b[2][4] == b[3][4] == b[4][4]:
        w = True
    elif b[0][0] == b[1][1] == b[2][2]:
        w = True
    elif b[1][1] == b[2][2] == b[3][3]:
        w = True
    elif b[2][2] == b[3][3] == b[4][4]:
        w = True
    elif b[0][4] == b[1][3] == b[2][2]:
        w = True
    elif b[1][3] == b[2][2] == b[3][1]:
        w = True
    elif b[2][2] == b[3][1] == b[4][0]:
        w = True
    elif b[1][0] == b[2][1] == b[3][2]:
        w = True
    elif b[2][1] == b[3][2] == b[4][3]:
        w = True
    elif b[2][0] == b[3][1] == b[4][2]:
        w = True
    elif b[0][1] == b[1][2] == b[2][3]:
        w = True
    elif b[1][2] == b[2][3] == b[3][4]:
        w = True
    elif b[0][2] == b[1][3] == b[2][4]:
        w = True
    elif b[3][0] == b[2][1] == b[1][2]:
        w = True
    elif b[2][1] == b[1][2] == b[0][3]:
        w = True
    elif b[2][0] == b[1][1] == b[0][2]:
        w = True
    elif b[4][1] == b[3][2] == b[2][3]:
        w = True
    elif b[3][2] == b[2][3] == b[1][4]:
        w = True
    elif b[4][2] == b[3][3] == b[2][4]:
        w = True
    else:
        w = False
    return w

def game1p5():
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
        l,b = x5()
        while True:
            board5(b)
            print(f'Player {k1}')
            c,n = ctrl5(l)
            if n == 0:
                break
            else:
                pass
            a = k1
            b = mod_jovel.changingb(c,b,a)
            l = mod_jovel.changingl(n,l)
            w = wins5(b)
            if w:
                break
            elif sum(l) == 0:
                break
            else:
                pass
            board5(b)
            print(f'Player {k2}')
            c,n = ctrl5(l,1)
            sleep(1)
            a = k2
            b = mod_jovel.changingb(c,b,a)
            l = mod_jovel.changingl(n,l)
            w = wins5(b)
            if w:
                break
            elif sum(l) == 0:
                break
            else:
                pass
        if n == 0:
            break
        board5(b)
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

def game2p5():
    a = 'Y'
    while a == 'Y':
        l,b = x5()
        while True:
            board5(b)
            print('Player O')
            c,n = ctrl5(l)
            if n == 0:
                break
            else:
                pass
            a = 'O'
            b = mod_jovel.changingb(c,b,a)
            l = mod_jovel.changingl(n,l)
            w = wins5(b)
            if w:
                break
            elif sum(l) == 0:
                break
            else:
                pass
            board5(b)
            print('Player X')
            c,n = ctrl5(l)
            if n == 0:
                break
            else:
                pass
            a = 'X'
            b = mod_jovel.changingb(c,b,a)
            l = mod_jovel.changingl(n,l)
            w = wins5(b)
            if w:
                break
            elif sum(l) == 0:
                break
            else:
                pass
        if n == 0:
            break
        board5(b)
        if w:
            print(f'{a} wins')
        else: 
            print('Oh, you tied haha!')
        while True:
            a = mod_jovel.readstr('Do you want to play again? [Y/N] ').strip().upper()[0]
            if a == 'Y' or a == 'N':
                break
            else:
                print(f'\033[0;31mERROR! Choose only Y or N.\033[m')
    print('Finishing... Thanks for playing ;)')
    sleep(1)

game1p5()






