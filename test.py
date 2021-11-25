def ctrl():
    n = int(input('Choose a number: '))
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
    return c

def changing(c,b,k):
    b[c[0]][c[1]] = k
    return b

def x3():
    b = [[1,2,3],[4,5,6],[7,8,9]]
    return b

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
    
def game():
    b = x3()
    a = 'Y'
    while a == 'Y':
        while True:
            board3(b)
            c = ctrl()
            a = 'O'
            b = changing(c,b,a)
            board3(b)
            w = wins(b)
            if w:
                break
            else:
                pass
            board3(b)
            c = ctrl()
            a = 'X'
            b = changing(c,b,a)
            board3(b)
            w = wins(b)
            if w:
                break
            else:
                pass
        print(f'{a} wins')
        a = input('Do you want to play again? [Y/N] ').strip().upper()[0]

game()




