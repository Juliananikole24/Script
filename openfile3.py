# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 18:35:57 2022

@author: Usuario
"""
lista=[]
file=open("C:/Users/Usuario/Documents/Juliana/Curso Phyton/clase 8 febrero 11/devices.txt")
for a in file:
    a=a.strip("\n")
    lista.append(a)
    #print(a)
file.close()
print(lista)
