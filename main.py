def verificare_cuvant(tranzitii, stare_initiala, stari_finale, cuvant):
    stare_curenta = stare_initiala
    drum = []
    for c in cuvant:
        tranzitie = (stare_curenta, c)
        if tranzitie not in tranzitii:  # verifica daca exista o tranzitie pentru caracterul curent
            return False
        stare_curenta = tranzitii[tranzitie] # actualizeaza starea curenta
        drum.append(tranzitie)  # adauga tranzitia la drum
    # verifica daca starea curenta este una finala
    if stare_curenta in stari_finale:
        print("Cuvantul este acceptat de automat.")
        print("Drumul folosit pentru acceptare:", end=" ")
        for tranzitie in drum:
            print(f"({tranzitie[0]}, {tranzitie[1]})", end=" ")
        print()
        return True
    else:
        return False

# citirea automatului din fisier
with open("fisier.txt", "r") as f:
    # citirea starilor si a simbolurilor alfabetului
    stari = set(f.readline().strip().split())
    simboluri = set(f.readline().strip().split())
    # citirea starilor finale
    stari_finale = set(f.readline().strip().split())
    # citirea tranzitiilor
    tranzitii = {}
    for linie in f:
        stare1, caracter, stare2 = linie.strip().split()
        tranzitii[(stare1, caracter)] = stare2
# citirea cuvantului de la tastatura
cuvant = input("Introduceti cuvantul: ")
# verifica daca cuvantul este acceptat de automat si afiseaza drumul folosit pentru acceptare
if not verificare_cuvant(tranzitii, "q0", stari_finale, cuvant):
    print("Cuvantul nu este acceptat de automat.")