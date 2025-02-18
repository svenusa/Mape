import csv

with open ("pdb_pvnmaksataji_odata.csv", encoding = "utf-8") as file:
    csv1 = csv.reader(file)#izveido csv objektu
    saraksts = list(csv1)
    print("Izdruka ir: ", saraksts, "\n")#izvada csv datus masīvā

    print("Datnes nosaukums ir: ", file.name, "\n")

    #masīva garums
    garums=len(saraksts)
    print("Masīva garums", garums, "\n")

    #pirmais elements
    pirmais = saraksts[1]
    print("Saraksta pirmais elements ir:", pirmais)

    pirmie7 = saraksts [1:7]
    print("Pirmie septiņi elementi ir: ", pirmie7)

    #izvadīt noteikta kārtras numura elementu
    def elements(file):
        file = open("pdb_pvnmaksataji_odata.csv", encoding = "utf-8")
        csv1 = csv.reader(file)
        masivs = list(csv1)
        ievade = input("Ievadi elementu numuru: ")
        numurs = int (ievade)
        elements = masivs[numurs - 1] # -1 jo skaitīsāna
        print("Izvēlētais elements ir: ", elements)
        print ("\n")

elements(file)