e1 = float(input("altura 1: "))
e2 = float(input('altura 2: '))
e3 = float(input('altura 3: '))
if e1 == e2 or e1 == e3 or e2 == e3:
    print("Há pelo menos duas pesoas com estaturas iguais.")
else:
    if e1 > e2 and e1 > e3:
        print("A maior altura é : {:.2f}m".format(e1))
    elif e2 > e1 and e2 > e3:
        print("A maior altura é : {:.2f}m".format(e2))
    else:
        print('A maior altura é : {:.2f}m'.format(e3))
