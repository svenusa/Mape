#izveidot vārdnīcu
tulkojums =  {"table":"galds", "book":"grāmata","school":"skola" }
print(tulkojums["table"])
print(tulkojums["table"], tulkojums["book"])

#saliktā vārdnīca
sekmes={
    "Jānīts":{"sem1":8, "sem2":7},
    "Anniņa":{"sem1":6, "sem2":9},
    "Pēterīts":{"sem1":7, "sem2":8}
}
ann = sekmes["Anniņa"]
print(ann)
ann2 = ann["sem2"]
print(ann2)
#Īsāks pieraksts
print(sekmes["Anniņa"]["sem1"])

#elementu pievienošana vārdnīcai
pilsetas = {"Igaunija":"Tallina", "Latvija":"Rīga", "Lietuva":"Viļņa"}
print(pilsetas)
pilsetas["Polija"] = "Varšava"
print(pilsetas)#izvada 4 pilsētu nosaukumus

#vārdnīcas garums
tulkojums =  {"table":"galds", "book":"grāmata","school":"skola", "car":"mašīna" }
print("Vārdnīcas garums ir", len(tulkojums))#nosaka garumu

#vārdnīcas papildināšana
gramata = {"Nosaukums":"Haarijs Poters", "Autors":"Roulinga"}
print(gramata)
papildus_dati={"gads":1997, "Žanrs":"Romāns", "Izdevniecība":"Zvaigzne"}
gramata.update(papildus_dati)
print(gramata)

#Ievada vērtējumu, izdrukā skaidrojumu
atzimes_skaidrojums = {
10:"Izcili",
9:"Teicami",
8:"Ļoti labi",
7:"Labi",
6:"Gandrīz labi",
5:"Viduvēji",
4:"Gandrīz viduvēji",
3:"Vāji",
2:"Ļoti vāji",
1:"Ļoti, ļoti vāji"
}
#ievada veselu skaitli no 1 līdz 10
while True:
    try:
        ievade = int(input("Ievadiet veselu skaitli no 1 līdz 10 "))
        if 1 <= ievade <= 10:
            break
        else:
            print("Ievadītais skaitlis nav no 1 līdz 10. Lūdzu ievadiet pareizu skaitli.")
    except ValueError:
        print("Ievadītajam vērtējumam jābūt veselam skaitlim.")

#izvadam skaidrojumu
skaidrojums = atzimes_skaidrojums[ievade]
print(f"Vārdiskais skaidrojums ievadītajam vērtējumam {ievade} ir: {skaidrojums}" )