from pkgs.operations import *
from pkgs.area import *

print("Hi, What are the operations you would like to perform?")
print("Kindly use this keymap!")
print("1.factorial 2.cube 3.area 4.perimeter")

z = int(input())

if z ==1:
    fact(int(input("WHat's the num")))
elif z==2:
    cube(int(input("WHat's the num")))
elif z ==3:
    area(int(input("WHat's the side")))
elif z==4:
    perimeter(int(input("WHat's the side")))




