productos = {"pan":1.40, "huevos":2.30, "cebolla":0.85, "aceite":4.35}
p = input("Producto:")
n_u = int (input("Numero de unidades:"))
if p == "pan":
    n = (productos["pan"]*n_u)
    print ("El precio total es de:", n)
if p == "huevos":
    h = (productos["huevos"]*n_u)
    print ("El precio total es de:", h)
if p == "cebolla":
    c = (productos["cebolla"]*n_u)
    print ("El precio total es de:", c)
if p == "aceite":
    a = (productos["aceite"]*n_u)
    print ("El precio total es de:", a)
elif p != "pan" and "huevos" and"cebolla" and"aceite":
    print ("¡No se encuentra el producto!")