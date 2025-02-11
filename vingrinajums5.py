saraksts = [int(sk) for sk in input ("Ievadi skaitļus, atdalot ar atstarpi: "). split()]
for i in range (len(saraksts)):
    if saraksts[i] ==saraksts[i-1]:
        print (saraksts[i], saraksts [i-1])
 #nomaini plusus uz mīnusiem un saliec atstapres

