from datetime import *
from itertools import filterfalse
from pickle import FALSE 
def date(d:int, m:int,y:int)-> bool:
    try:
        print(date(y,m,d))
        flag=True
    except:
        print("Viga")
        flag=False
    return flag




def arithmetic(arv1:float,tehe:str,arv2:float)->any:
    """any = означает 
    """
    if tehe== "+":
       vastus=arv1+arv2
    elif tehe== "-":
       vastus=arv1-arv2
    elif tehe== "*":
       vastus=arv1*arv2
    elif tehe== "/":
       if arv2==0:
           vastus="DIV0"
       else:
           vastus=arv1/arv2
    else:
        vastus="Tundmatu tehe"

    return vastus

#2
# is_year_leap(aasta: int)->bool:
#    """
#    """
#    if aasta%4==0:
#        t=True
#    else:
#        t=False
#
#    return t

#3
def square(a:float)->float:
    """pindala läbimõõt diagonale leidmine
    """
    p=4*a
    s=a*a
    d=(a**2)/2
    return p,s,d

#4
def season(month:float)->str:
    """
    """
    if month == 12 or 1 <= month <= 2:
       print("Зима")
    elif  3 <= month <= 5:
       print("Весна")
    elif 6 <= month <= 8:
       print("Лето")
    elif 9 <= month <= 11:
       print("Осень")
    else:
       print("Viga!")
n = int(input("Введите номер месяца 1-12: "))
season(n)

#5
def bank(b:float, a:int)->float:
    """
    """
    for i in range (a):
        b=b+b*0.1
    return b

#6
def is_prime(a:float)->str:
    if a % a == 0 and a != 0:
        return True
    else:
        return False

def is_prime(arv:float)->str:
    """
    """
    flag=True
    for i in range(2,arv):
        if arv%i==0:
            flag=False
            break
    return flag

from datetime import * 


