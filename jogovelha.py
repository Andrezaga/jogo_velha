import mod_jovel

while True:
    c = mod_jovel.menu1()
    if c == 1:
        while True:
            c = mod_jovel.menu2()
            if c == 1:
                while True:
                    c = mod_jovel.menu3()
                    if c == 1:
                        mod_jovel.game1p3()
                    elif c == 2:
                        mod_jovel.game1p4()
                    elif c == 3:
                        mod_jovel.game1p5()
                    elif c == 0:
                        break
            elif c == 2:
                while True:
                    c = mod_jovel.menu3()
                    if c == 1:
                        mod_jovel.game2p3()
                    elif c == 2:
                        mod_jovel.game2p4()
                    elif c == 3:
                        mod_jovel.game2p5()
                    elif c == 0:
                        break
            elif c == 0:
                break
    elif c == 0:
        print('Finishing... See you ;)')
        break



