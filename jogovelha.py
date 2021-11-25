import mod_jovel

c = mod_jovel.menu1()
if c == 1:
    c = mod_jovel.menu2()
    if c == 1:
        pass
    if c == 2:
        c = mod_jovel.menu3()
        if c == 1:
            mod_jovel.game()
        if c == 2:
            pass
        if c == 3:
            pass
elif c == 2:
    print('Finishing... See you ;)')



