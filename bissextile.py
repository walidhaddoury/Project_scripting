year = int(input("Entrez l annee a verifier:"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("L'annee est une annee bissextile!")
else:
    print("L'annee n'est pas une annee bissextile!")
