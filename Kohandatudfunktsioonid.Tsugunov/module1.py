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

def is_year_leap(aasta: int)->bool:
    """
    """
    if aasta%4==0:
        t=True
    else:
        t=False

    return t
        

def square(a):
    #
	p=4*a
	s=a*a
	d=(a**2)/2
	d= d**2
	b=(p, s, d)
print(square(8))

