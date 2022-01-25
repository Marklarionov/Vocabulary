from MyModule import *
rusl=[]
engl=[]
rusl=failist_lugemine("rus.txt",rusl)
engl=failist_lugemine("ang.txt",engl)
print("This is a Russian-English and English-Russian dictionary.")
while True:
    print("""Choose what you want to do")
    1 - Show all words")
    2 - To choose a Russian-English dictionary")
    3 - To choose a English-Russian dictionary")
    4 - Add new word to dictionary")
    5 - Correct mistake")
    6 - To exit the dictionary")""")
    menu=int(input("Your choise: "))
    if menu==1:
        print(rusl)
        print(engl)
    elif menu==2:
        word= input("Choose the word you want to translate: ")
        indx = rusl.index(word)
        print(f"{word} - {engl[indx]}")
    elif menu==3:
        word= input("Choose the word you want to translate: ")
        indeks = engl.index(word)
        print(f"{word} - {rusl[indx]}")
    elif menu==4:
        rusl=add_word("rus.txt",input("Новое слово: "))
        engl=add_word("ang.txt",input("New word: "))
    elif menu==5:
        print()
    elif menu==6:
        exit()
    else:
        print("Incorrect Value")
