def bosluk(adet):
    for a in range(int(adet)):
        print(" ",end="")
def sag(adet):
    for a in range(int(adet)):
        print("/",end="")
def sol(adet):
    for a in range(int(adet)):
        print("\\",end="")
def atla(adet):
    for a in range(int(adet)):
        print()

def üst(cap):
    baslanginc = cap/2-1
    for a in range(int(cap/2)):
        bosluk(baslanginc-a)
        sag(1)
        bosluk(a*2)
        sol(1)
        atla(1)

def alt(cap):
    baslanginc = cap-2
    for a in range(int(cap/2)):
        bosluk(a)
        sol(1)
        bosluk(baslanginc-a*2)
        sag(1)
        atla(1)
def elmas(cap):
    üst(cap)
    alt(cap)
while True:
    boyut = int(input("Elmasın çapını giriniz : "))
    if boyut==0:
        quit()
    elmas(boyut)