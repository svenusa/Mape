import csv

with open ("Programas valodas1(in).csv", "r") as file:
    reader = csv.DictReader(file)
    counts = ()
    for row in reader:
        favorite = row["Valoda"]
        if favorite in counts:
            counts[favorite] +=1
        else:
            counts[favorite] = 1

for favorite in counts:
    print(f"{favorite}: {counts[favorite]}")
    #Python = 0
    #C = 0
    #Java = 0
    #for row in reader:
        #favorite = row["Valoda"]
        #if favorite == "Python":
         #   Python += 1
        #elif favorite == "C":
         #   C += 1
        #elif favorite == "Java":
            #Java += 1

print(f"Python: {Python} ")
print(f"C: {C} ")
print(f"Java: {Java} ")

    #for row in reader:
        #favorite = row["Valoda"]
        #print(favorite)
        #print(row[1])