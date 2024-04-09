#Alprogramok
def beker():
    lista=[]
    with open ("adatok.txt","r",encoding="UTF-8") as fm:
        for sor in fm:
            lista.append(float(sor.strip()))
    return lista

def osszegez1(l):
    szum=0
    for elem in l:
        szum+=elem
    return szum

def osszegez2(l):
    osszeg=0
    for elem in l:
        if elem!=int(elem):
            osszeg+=elem
    return int(osszeg*100)/100

def kereses(l):
    legnagyobb=0
    for elem in l:
        if elem%1==0 and elem > legnagyobb:
            legnagyobb=elem
    return legnagyobb

def kivalasztas1(l):
    index=0
    for elem in l:
        if elem==9:
            return index
        index+=1
    return -1

def kivalasztas2(l):
    utolso_tiznelt=-1
    for i in range(len(l)):
        if l[i] > 10:
            utolso_tiznelt=i
    return utolso_tiznelt

def osszegez3(l):
    db=0
    for _ in range(len(osszegek)):
        db+=1
    fizetes=db*0.5
    return fizetes+sum(osszegek)

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

def osszegzes0(o):
    osszeg=sum(o)+8.23  
    return osszeg
  
def eldontes2(o):
    i=0
    volt=False
    while o[i]<=10 and i<len(o):
        i+=1

    if i<len(o):
        volt=True

    return i+1,volt

def eldontes3(o):
    i=0
    volt=False
    while i<len(o) and o[i]%5!=0:
        i+=1

    if i<len(o):
        volt=True

    return volt

  def kiir(ossz,o_v_m,h_p_o,l_a_sz,h_e_f_k,u_t_t,a_h_f,b,d,f,h,j,j_volt_e,l):
    print(ossz)
    if b:
        print("Volt olyan, hogy a pincér valamit vett.")
    else:
        print("Nem volt olyan, hogy a pincér valamit vett.")
    print(f"{o_v_m} van benne az óra végén")
    print(f"{d} alkalommal kapot biztosan penny-t is.")
    print(f"{h_p_o} pennyt kapott összesen.")
    print(f"{f} esetben kapott legalább öt fontot.")
    print(f"{l_a_sz} állt a legnagyobb számlán, amit fizettek a pincérnél.")
    print(f"Ha az óra elején már volt 8 font 23 penny a tárcájában, {h} pénz volt benne az óra végén.")
    print(f"{h_e_f_k}.  vendég fizetett 9 fontot.")
    if j_volt_e:
        print(f"A {j}. vendég volt az élső aki 10 fontnál többet fizetett.")
    else:
        print("Nem volt olyan vendég aki 10 fontnál többet fizetett.")
    print(f"{u_t_t}. vendég volt az utolsó, aki tíz fontnál többet fizetett.") 
    if l:
        print("Volt olyan vendég, akinek módjában állt csupa ötfontossal kiegyenlíteni a számlát.")
    else:
        print("Nem volt olyan vendég, akinek módjában állt csupa ötfontossal kiegyenlíteni a számlát.")
    print(f"{a_h_f} bevétellel zárta az órát.")

#Főprogram
#Input
osszegek=beker()

#Számolás 
b=eldontes(osszegek)
d=megszamolas(osszegek)
f=megszamolas2(osszegek)
h=osszegzes0(osszegek)
j,j_volt_e=eldontes2(osszegek)
l=eldontes3(osszegek)
ora_vegen_mennyi=osszegez1(osszegek)
hany_penny_osszesen=osszegez2(osszegek)
legnagyobb_a_szamlan=kereses(osszegek)
hanyadik_ember_fizetett_kilencet=kivalasztas1(osszegek)
utolso_tiznel_tobb=kivalasztas2(osszegek)
adott_hozza_fel=osszegez3(osszegek)

#Output
kiir(osszegek,ora_vegen_mennyi,hany_penny_osszesen,legnagyobb_a_szamlan,hanyadik_ember_fizetett_kilencet,utolso_tiznel_tobb,adott_hozza_fel,osszegek,b,d,f,h,j,j_volt_e,l)



