#izveido kopu
#vārdu saraksts
pirkumu_grozs = {"āboli", "zemenes", "bumbieri", "Ķirši"}
#izveido kopu
kopa=set(pirkumu_grozs)
#print(pirkumu_grozs)
print (kopa)
#nejauša secība

#elementi atkārtoties nevar
cipari={2,3,4,5,6,7,2}
print(cipari)

#pievienot kopai elementu
prieksmeti = {"matematika", "latv val", "bioloģija", "ģeogrāfija"}
prieksmeti.add("krievu val") #pievieno elementu, jo, kurš būtu minējis, ka add nozīmē pievienot?
print(prieksmeti)

#kopu pievienošana
prieksmeti = {'fizika', 'matematika'}
prieksmeti.update({'Ķīmija', 'bioloģija'}) #pievieno kopu
print(prieksmeti)

#kopu apvienošana
gadalaiki = {'rudens', 'pavasaris'}
gadalaiki1 = {'ziema', 'vasara'}
gadalaiki = gadalaiki|gadalaiki1 #apvieno
print(gadalaiki)

#izdzēst kopu elementu
auto ={'opel', 'audi', 'volvo'}
print(auto)
auto.discard('audi') #dzēš
print(auto)

#kopas šķēlums
sk1 = {100,2,31,74,65}
sk2 = {65,74,8,9,10}
skelums = sk1.intersection(sk2)
print(skelums)