#!/usr/bin/python
print("""

 _______       ______         _          ______     ____  ____          _        ___  ____   
|_   __ \    .' ____ \       / \        |_   _ \   |_  _||_  _|        / \      |_  ||_  _|  
  | |__) |   | (___ \_|     / _ \         | |_) |    \ \  / /         / _ \       | |_/ /    
  |  __ /     _.____`.     / ___ \        |  __'.     \ \/ /         / ___ \      |  __'.    
 _| |  \ \_  | \____) |  _/ /   \ \_     _| |__) |    _|  |_       _/ /   \ \_   _| |  \ \_  
|____| |___|  \______.' |____| |____|   |_______/    |______|     |____| |____| |____||____| 
                                                                                             by AK                 
   
""")                                                           
print("#Author AK")
print("#This will only work in some rsa ,simple rsa,")
print("#you will have to install those if you didn't have it")
print("#from Crypto.Util.number import *")
print("#import gmpy")
print("#from Crypto.PublicKey import RSA ")
from Crypto.Util.number import *
import gmpy
from Crypto.PublicKey import RSA
p=int(input("Enter P :"))
q=int(input("Enter q :"))
e=int(input("Enter e:"))
ct=int(input("Enter ciphertext :"))
n=p*q
phin=(p-1)*(q-1)
d=gmpy.invert(e,phin)
m=hex(pow(ct,d,n))[2:]
print(m.decode('hex'))
