def failist_lugemine(f:str,l:list):
    """
    """
    fail=open(f,"r" ,enconding="utf-8-sig")
    for rida in fail:
        l.append(rida.strip())#"\n"
    fail.close()
    return l

def fail_salv(f:str,l:list):
    """
    """
    fail=open(f,"w")
    for el in l:
        fail.write(el+"\n")
    fail.close()

def rida_salvestamine(f:str,rida:str):
    """Üks sõna või lause(rida) salvestamine
    failisse
    :param str f: fail kuku salvestame
    :param str rida: sõna, mis vaja salvestada failisse
    """
    fail=open(f,"a")
    fail.write(rida+"\n")
    fail.close()

def add_word(f:str,rida:str)->list:
    """
    :param str file: faili nimetus
    :param str x: lisatav sõna
    """
    l=[]
    with open(f,"a",enconding="utf-8-sig") as fail:
        fail.write(rida+"\n")
    l=failist_lugemine(f)
    return l