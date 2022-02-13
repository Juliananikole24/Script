# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 18:58:56 2022

@author: Usuario
"""

file=open("C:/Users/Usuario/Documents/Juliana/Curso Phyton/clase 8 febrero 11/devices.txt","a")
while True:
   newItem = input("Enter device name: ")
   if newItem == "exit":
        print("All done!")
        break
   file.write(newItem + "\n")
file.close()


