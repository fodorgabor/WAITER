#Alprogramok
def beker():
    lista=[]
    with open ("adatok.txt","r",encoding="UTF-8") as fm:
        for sor in fm:
            lista.append(float(sor.strip()))
    return lista

def eldontes(o):
    volt=False
    i=0
    while i<len(o) and not (o[i]<0):
        i+=1
        
    if i<len(o):
        volt=True
    return volt

def megszamolas(o):
    db=0
    for elem in o:
        if elem%1!=0:
            db+=1
    return db 
    
def megszamolas2(o):  
    db=0
    for elem in o:
        if elem >= 5:
            db+=1
    return db

def osszegzes(o):
    osszeg=sum(o)+8.23  
    return osszeg
  
def kiir(ossz,b,d,f,h):
    print(ossz)
    if b:
        print("Volt olyan, hogy a pincér valamit vett.")
    else:
        print("Nem volt olyan, hogy a pincér valamit vett.")
    print(f"{d} alkalommal kapot biztosan penny-t is.")
    print(f"{f} esetben kapott legalább öt fontot.")
    print(f"Ha az óra elején már volt 8 font 23 penny a tárcájában, {h} pénz volt benne az óra végén.")
#Főprogram
#Input
osszegek=beker()

#Számolás 
b=eldontes(osszegek)
d=megszamolas(osszegek)
f=megszamolas2(osszegek)
h=osszegzes(osszegek)
j=1
l=1
#Output
kiir(osszegek,b,d,f,h)
