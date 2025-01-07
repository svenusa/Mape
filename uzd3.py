#saraksts
skaitļi=[1,2,3,4,5,6,7,8,9,10]
#kāpina elementus kvadrātā
kvadrats=[x**2 for x in skaitļi]
#apvieno sarakstu un kvadrātus kopā
apvienotais= skaitļi + kvadrats
#printē apvienoto
print(apvienotais)
mazākais = min(apvienotais)
lielākais = max(apvienotais)
print("Lielākais", lielākais)
print("Mazākais", mazākais)

skaitlis=list(range(1,11))
summa = sum(skaitlis)
print("summa", summa)

pilsetas = ["Rīga", "Londona", "Parīze", "Liepāja", "Ķekava"]
print(pilsetas)
garakais = max(pilsetas, key=len)
mazakais = min(pilsetas, key=len)
print("Garākāis pilsētas nosaukums", garakais)
print("Mazākais pilsētas nosaukums", mazakais)