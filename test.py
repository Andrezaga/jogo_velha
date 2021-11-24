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



    




