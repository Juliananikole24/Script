# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 19:30:50 2022

@author: Usuario
"""


nombre=input("Ingrese su nombre:")
apellido=input("Ingrese su apellido")
direccion=input("Ingrese su direccion")
edad=int (input("Ingrese su edad"))
space=""
edad=int(input("Ingrese su edad"))
if edad>=10 and edad<=20:
    print("la edad es Adolescente")
elif edad>=20 and edad<=30:
    print("la edad es de infante")
else:
    print("El dato ingresado no es la edad verdadera")

print("Su nombre es" ,nombre,space,apellido + "su dirección es",direccion + "su edadd es" ,edad)


