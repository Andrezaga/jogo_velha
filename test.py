from random import randint
from time import sleep

def ctrl(l,a=0):
    if a == 1:
        while True:
            n = randint(1,9)
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
    else:
        print('Choose an integer number')
    return c, n

def changingb(c,b,k):
    b[c[0]][c[1]] = k
    return b

def changingl(n,l):
    l[n-1] = 0
    return l

def x3():
    l = [1,2,3,4,5,6,7,8,9]
    b = [[1,2,3],[4,5,6],[7,8,9]]
    return l,b

def board3(b):
    print('-'*13)
    for i in b:
        for j in i:
            print(f'| {j}',end=' ')
        print('|')
        print('-'*13)

def wins(b):
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
    
def game1p():
    a = 'Y'
    while a == 'Y':
        k1 = input('Choose a symble: [O/X] ').strip().upper()[0]
        if k1 == 'O':
            k2 = 'X'
        elif k1 == 'X':
            k2 = 'O'
        l,b = x3()
        while True:
            board3(b)
            print(f'Player {k1}')
            c,n = ctrl(l)
            a = k1
            b = changingb(c,b,a)
            l = changingl(n,l)
            w = wins(b)
            if w:
                break
            else:
                pass
            board3(b)
            print(f'Player {k2}')
            c,n = ctrl(l,1)
            sleep(1)
            a = k2
            b = changingb(c,b,a)
            l = changingl(n,l)
            w = wins(b)
            if w:
                break
            else:
                pass
        board3(b)
        print(f'{a} wins')
        a = input('Do you want to play again? [Y/N] ').strip().upper()[0]
    print('Finishing... See you ;)')

game1p()




