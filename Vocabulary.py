from MyModule import *
from random import *
rusl=[]
engl=[]
rusl=failist_lugemine("rus.txt",rusl)
engl=failist_lugemine("ang.txt",engl)
print("This is a Russian-English and English-Russian dictionary.")
while True:
    print("""Choose what you want to do
    1 - Show all words
    2 - To choose a Russian-English dictionary
    3 - To choose a English-Russian dictionary
    4 - Add new word to dictionary
    5 - Correct mistake
    6 - Test
    7 - To exit the dictionary""")
    menu=int(input("Your choise: "))
    if menu==1:
        print(rusl)
        print(engl)
        print()
    elif menu==2:
        word= input("Choose the word you want to translate from Russian into English: ")
        indx = rusl.index(word)
        print()
        print(f"{word} - {engl[indx]}")
        print()
    elif menu==3:
        word= input("Choose the word you want to translate from English to Russian: ")
        indx = engl.index(word)
        print()
        print(f"{word} - {rusl[indx]}")
        print()
    elif menu==4:
        slovo = input("Write the word you want to add: ")
        if slovo in engl:
            print("This word has already been added in english dictionary")
        else:
            add_word("ang.txt",slovo,engl)
        slovo = input("write the Russian word you want to add: ")
        if slovo in rusl:
            print("This word has already been added in russian dictionary")
        else:
            add_word("rus.txt",slovo,rusl)
        print()
    elif menu==5:
        ans=input("Which dictionary has the error eng or rus?")
        if ans == "eng":
            word=input("Write the word you want to correct: ")
            correct(word,engl)
        elif ans == "rus":
            word = input("Write the word you want to correct: ")
            correct(slovo,rusl)
        else:
            print("Invalid data type!")
        print()
    elif menu==6:
        print("You need to write the correct translation for the words that will be displayed")
        score = 0
        for i in range(len(rusl)):
            number = randint(1,2)
            if number == 1:
                score = test(score,rusl,engl)
            else:
                score = test(score,engl,rusl)
        mark = score * 100 / len(rusl)
        print(f"Your {score}/{len(rusl)} points")
        if mark >= 90:
            print("Good, mark 5!")
        elif mark >= 75 and mark <= 90:
            print("Good, mark 4!")
        elif mark >= 50 and mark <= 75:
            print("Good, mark 3!")
        else:
            print("2 is bad, try better!")
        print()
    elif menu==7:
        exit()
    else:
        print("Invalid data type!")
