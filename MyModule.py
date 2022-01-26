from random import *
def failist_lugemine(f:str,l:list):
    """
    """
    fail=open(f,"r" ,encoding="utf-8-sig")
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

def add_word(f:str,word:str,l:list)->list:
    """
    :param str file: faili nimetus
    :param str x: lisatav sõna
    """
    l=[]
    with open(f,"a",encoding="utf-8-sig") as fail:
        fail.write(word+"\n")
    l=failist_lugemine(f,l)
    return l
def correct(word:str,l:list):
    """
    """
    for i in range(len(l)):
        if l[i] == word:
            new_word = word.replace(word,input("New word: "))
            l.insert(i,new_word)
            l.remove(word)
def test(score:int,l:list,l2:list)->int:
    """
    """
    word = choice(l)
    otvet = input(f"{word} >>> ")
    if otvet in l2: 
        if l2.index(otvet) == l.index(word):
            score += 1
            print("Good")
    else:
        print("Bad")
    return score
