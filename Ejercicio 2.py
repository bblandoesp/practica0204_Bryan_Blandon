nombre = input ("Nombre:")
edad = int (input ("Edad:"))
direccion = input ("Direccion:")
telefono = input ("Telefono:")
datos = {"nombre": nombre, "edad": edad, "direccion": direccion, "telefono": telefono}
print (datos["nombre"], "tiene", datos["edad"], "años", ",", 
       "vive en", datos["direccion"], "y su numero de telefono es", datos["telefono"])