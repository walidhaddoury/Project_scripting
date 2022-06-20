import sys

while True:
    annee = int(input("Entrez une année : "))
    if annee % 4 == 0 and annee % 100 != 0 or annee % 400 == 0:
        print("L'année", annee, "est bissextile.")
    else:
        print("L'année", annee, "n'est pas bissextile.");
    if input("Voulez vous continuer ? (o/n") == "n":
        sys.exit()
    else:
        continue