from MyModule import *
rusl=[]
engl=[]
rusl=failist_lugemine("rus.txt",rusl)
engl=failist_lugemine("ang.txt",engl)
print("This is a Russian-English and English-Russian dictionary.")

while True:
    print("Choose what you want to do")
    print("1 - ")
    print("2 - to choose a Russian-English dictionary")
    print("3 - to choose a English-Russian dictionary")
    print("4 - Add new word to dictionary")
    print("5 - To exit the dictionary")
    menu=int(input("Your choise: "))
    if menu==1:
        print(rusl)
        print(engl)
    elif menu==2:
        print()
    elif menu==3:
        print()
    elif menu==4:
        rusl=add_word("rus.txt",input("Новое слово: "))
        engl=add_word("ang.txt",input("New word: "))
    elif menu==5:
        print()
    else:
        print("Incorrect Value")