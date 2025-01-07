#noteikt saraksta garumu nozīmē noteikt elementu skaitu sarakstā
saraksts=[1,5,12,3,15]
print (saraksts)
print('garums', len(saraksts))

#pielikt elementu saraksta beigās, dinamiski palielinot sarakstu
saraksts=[1,5,12,3,15]
print (saraksts)
saraksts.append('pele')
print (saraksts)

#Ievieto elementu noteiktā vietā
saraksts=[1,5,12,3,15]
print (saraksts)
saraksts.insert(0,"zaķis")
print (saraksts)

#apgriež otrādāk
saraksts=[1,5,12,3,15]
print (saraksts)
saraksts.reverse()
print (saraksts)

#noņemt elementu
saraksts=[1,5,12,3,15]
print (saraksts)
saraksts.pop(3)
print (saraksts)

#noņemt konkrētu elementu elementu
saraksts=[1,5,12,3,15]
print (saraksts)
saraksts.remove(3)
print (saraksts)

#nomaina elementu sarakstā
saraksts=[1,5,12,3,15]
print (saraksts)
saraksts[0]=1
saraksts[1]=5
saraksts[2]=12
saraksts[3]='zemūdene'
saraksts[4]=15
print (saraksts)