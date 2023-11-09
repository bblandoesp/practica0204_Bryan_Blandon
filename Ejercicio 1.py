Cambios = {"EURO":"€", "DOLLAR":"$", "YEN":"¥"}
d = input ("Divisa:")
if d.upper () in Cambios.keys () or  d.upper () in Cambios.values ():
        print ("¡se encuentra entre las divisas!")
else:
    print ("¡No se encuentra entre las divisas!")