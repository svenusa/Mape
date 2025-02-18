import csv

with open ("busstops.csv", encoding = "utf-8") as file:
    csv1 = csv.reader(file)#izveido csv objektu
    saraksts = list(csv1)
    print("Izdruka ir: ", saraksts, "\n")#izvada csv datus masīvā

    print("Datnes nosaukums ir: ", file.name, "\n")

    #masīva garums
    garums=len(saraksts)
    print("Masīva garums", garums, "\n")

    #septitais elements
    septitais = saraksts[6]
    print("Saraksta septītais elements ir:", septitais)
