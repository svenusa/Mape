with open("Ziema.txt", encoding="utf-8") as file:
    saturs = file.read()
    print(file.name) #izdrukā datnes nosaukumu
    print(saturs) #izdrukā tekstu

    #izvada cik simboli ir tekstā
    numChar = len(saturs)
    print("Tekstā ir ", numChar, " simboli")

    #izvada vārdu skaitu tekstā
    WordCount = saturs.split() #split atgriež sadala vārdus skaitļu virknē
    print("Tekstā ir", len(WordCount), " vārdi.")

with open("Ziema.txt", "r", encoding="utf-8") as file:
    numLines = len(file.readlines())
    print("Rindas teksta failā:", numLines)
    print("\n")

file.close()