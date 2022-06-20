import sys


while True:
    year = int(input("Entrez une année : "))
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("L'année est bissextile")
    else:
        print("L'année n'est pas bissextile")
    again = input("Voulez vous continuer ? oui / non : ")
    if again == "non":
        break
    else:
        continue

