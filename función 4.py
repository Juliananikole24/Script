# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 19:22:13 2022

@author: Usuario
"""

def direction(ciudad,calle,barrio):
    print("La dirección de envio es: ")
    print("Sector La", barrio)
    print("En la calle", calle)
    print("En la ciudad de: ", ciudad)
    
cl=input("INgrese la calle: ")
ba=input("Ingrese el sector de domicilio: ")
ci=input("Ingrese la Ciudad: ")

direction(ci, cl, ba)
cl=cl.upper()
ci=cl.upper()
ba=ba.upper()
cl.replace("ú", "u")
print(cl)



