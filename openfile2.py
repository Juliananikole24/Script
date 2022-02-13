# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 18:15:40 2022

@author: Usuario
"""
"""
ELIMINA SALTOS
"""
file=open("C:/Users/Usuario/Documents/Juliana/Curso Phyton/clase 8 febrero 11/devices.txt")
for a in file:
    a=a.strip()
    print(a)
file.close()

"""
es para eliminar letras C
"""
file=open("C:/Users/Usuario/Documents/Juliana/Curso Phyton/clase 8 febrero 11/devices.txt")
for a in file:
    a=a.strip("C")
    print(a)
file.close()