# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 19:12:22 2022

@author: Usuario
"""

lista1=["Python",58,
        True,25.8,]
print(type(lista1))
print(len(lista1))
print(lista1)
print(lista1[0])
print(lista1[1])
print(lista1[2])
print(lista1[3])
print(lista1[-1])
print(lista1[-2])
print(lista1[-3])
tupla1=("Python",58,
        True,25.8,)
print(tupla1)
print(tupla1[0])
print(tupla1[1])
print(tupla1[2])
print(tupla1[3])
lista1[0]="Hola Python desde el CEC-EC" #lista si se puede cambiar
tupla1[0]="Hola Python desde el CEC-EC" #no es inmutable por eso no vale correr no cambia
del lista1[3]
del tupla1[3]

