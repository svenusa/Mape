with open("maksligaisIntelekts.txt", encoding="utf-8") as file:
    saturs = file.read()
    print(saturs) #izdrukā tekstu
    print(file.name) #izdrukā datnes nosaukumu

    #izvada pirmos 15 simbolus
    piecpadsmit = saturs[0:15]
    print("Pirmie piecpadsmit simboli ir: ", piecpadsmit)

    #izvada pirmo simbolu
    pirmais = saturs[0]
    print("Pirmais simbols", pirmais)

    #izvada pedejo simbolu
    pedejais = saturs[-1]
    print("Pēdejais simbols ir ", pedejais)

    #izvada cik simboli ir tekstā
    numChar = len(saturs)
    print("Tekstā ir ", numChar, " simboli")

    #izvada vārdu skaitu tekstā
    WordCount = saturs.split() #split atgriež sadala vārdus skaitļu virknē
    print("Tekstā ir", len(WordCount), " vārdi.")

#izvada rindas teksta failā
with open("maksligaisIntelekts.txt", "r", encoding="utf-8") as file:
    numLines = len(file.readlines())
    print("Rindas teksta failā: ", numLines)
    print("\n")

#izdrukā pirmo rindu
filename = "maksligaisIntelekts.txt"
def pirmarinda(filename):
    file = open("maksligaisIntelekts.txt", "r", encoding="utf-8")
    rinda1=file.readlines(1)
    print("Pirmā rinda ir: ", rinda1)
pirmarinda(filename)

file.close