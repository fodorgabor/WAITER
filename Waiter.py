def beker():
    lista=[]
    with open ("adatok.txt","r",encoding="UTF-8") as fm:
        for sor in fm:
            lista.append(sor)
    return lista

adatok=beker()