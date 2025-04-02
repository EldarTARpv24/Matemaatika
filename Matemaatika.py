import random 

tase = int(input("sisesta tase (1, 2, 3): "))
tase1 = random.randint(1, 2)
tase2 = random.randint(1, 4)
tase3 = random.randint(1, 2)
koikkusimused = 0
oiged = 0
while True:
    if tase < 1 or tase > 3:
        print("vale arv")
        break

    koikkusimused += 1  

    if tase == 1:
        num = random.randint(1, 10)
        num1 = random.randint(1, 10)

        if tase2 == 1:
            tasevastus = num - num1
            try:
                vastusinim = int(input(f"{num} - {num1} ="))
                if tasevastus == vastusinim:
                    oiged += 1  
                    print(" ")
                    print("õige")
                    print(" ")
                elif vastusinim == 00:
                    break
                else:
                    print(" ")
                    print("vale")
                    print(" ")
            except ValueError:
                print("error, input arv palun")

        elif tase1 == 2:
            tasevastus = num + num1
            try:
                vastusinim = int(input(f"{num} + {num1} ="))
                if tasevastus == vastusinim:
                    oiged += 1
                    print(" ")
                    print("õige")
                    print(" ")
                elif vastusinim == 00:
                    break
                else:
                    print(" ")
                    print("vale")
                    print(" ")
            except ValueError:
                print("error, input arv palun")
    elif tase == 2:
        num2 = random.randint(1, 20)
        num3 = random.randint(1, 20)
        if tase2 == 1:
            taseotv = num2 - num3
        elif tase2 == 2:
            taseotv = num2 + num3
        elif tase2 == 3:
            taseotv = num2 * num3
        elif tase2 == 4:
            taseotv = num2 / num3
        try:
            vastustase2 = float(input(f"{num2} {['-', '+', '*', '/'][tase2 - 1]} {num3} ="))
            if round(taseotv, 2) == round(vastustase2, 2):
                oiged += 1
                print(" ")
                print("õige")
                print(" ")
            elif vastustase2 == 00:
                break
            else:
                print(" ")
                print("vale")
                print(" ")
        except ValueError:
            print("error, input arv palun")
    elif tase == 3:
        num2 = random.randint(1, 100)
        num3 = random.randint(1, 100)

        if tase3 == 1:
            taseotv = num2 * num3
        elif tase3 == 2:
            if num3 == 0:
                print(" ")
                print("nulliga jagada ei saa")
                print(" ")
                continue
            taseotv = num2 / num3
        try:
            vastustase2 = float(input(f"{num2} {['*', '/'][tase3 - 1]} {num3} = "))
            if round(taseotv, 2) == round(vastustase2, 2):
                oiged += 1
                print(" ")
                print("õige")
                print(" ")
            elif vastustase2 == 00:
                break
            else:
                print(" ")
                print("vale")
                print(" ")
        except ValueError:
            print("error, input arv palun")

if koikkusimused > 0:
    prot = (oiged / (koikkusimused-1)) * 100 
    if prot < 60:
        hinne = 2
    elif 60 <= prot < 75:
        hinne = 3
    elif 75 <= prot < 90:
        hinne = 4
    else:
        hinne = 5

    print(" ")
    koikkusimused-=1 #et ei loeks 00 nagu vastust
    print(f"tulemus: {oiged}/{koikkusimused} {prot}%")
    print(f"hinne: {hinne}")
    print(" ")
else:
    print("dvoika za test")
