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

def kiir(ossz,o_v_m,h_p_o,l_a_sz,h_e_f_k,u_t_t,a_h_f):
    print(ossz)
    print(f"{o_v_m} van benne az óra végén")
    print(f"{h_p_o} pennyt kapott összesen.")
    print(f"{l_a_sz} állt a legnagyobb számlán, amit fizettek a pincérnél.")
    print(f"{h_e_f_k}.  vendég fizetett 9 fontot.")
    print(f"{u_t_t}. vendég volt az utolsó, aki tíz fontnál többet fizetett.")  
    print(f"{a_h_f} bevétellel zárta az órát.")

#Főprogram
#Input
osszegek=beker()
ora_vegen_mennyi=osszegez1(osszegek)
hany_penny_osszesen=osszegez2(osszegek)
legnagyobb_a_szamlan=kereses(osszegek)
hanyadik_ember_fizetett_kilencet=kivalasztas1(osszegek)
utolso_tiznel_tobb=kivalasztas2(osszegek)
adott_hozza_fel=osszegez3(osszegek)
#Számolás 

#Output
kiir(osszegek,ora_vegen_mennyi,hany_penny_osszesen,legnagyobb_a_szamlan,hanyadik_ember_fizetett_kilencet,utolso_tiznel_tobb,adott_hozza_fel)
