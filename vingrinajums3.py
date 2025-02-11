sk=int(input("Ievadi skaitli (0 - beigt): "))
summa=0
skaits=0
while sk!=0:
    summa += sk
    skaits +=1
    sk=int(input("Ievadi skaitli (0 - beigt):" ))
print("Visu ievadīto skatļu vidējais aritgmētiskais ir", summa/skaits)
#nebija definēts skaits, un nebija atkāpes saliktas 5, 6 un 7 rindā
