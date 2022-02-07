# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 19:20:47 2022

@author: Usuario
"""

acl=int(input("Ingrese el # de ACL"))
if acl>=1 and acl<=99:
    print("la ACL es Estandar")
elif acl>=100 and acl<=199:
    print("la ACL es Extendida")
else:
    print("El dato ingresado no es de un ACL")
    
    
    