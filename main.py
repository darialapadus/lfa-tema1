def verificare_cuvant(tranzitii, stare_initiala, stari_finale, cuvant):
    stare_curenta = stare_initiala
    drum = []
    for c in cuvant:
        tranzitie = (stare_curenta, c)
        if tranzitie not in tranzitii:
            return False
        stare_curenta = tranzitii[tranzitie]
        drum.append(tranzitie)
    if stare_curenta in stari_finale:
        print("Cuvantul este acceptat de automat.")
        print("Drumul folosit pentru acceptare:", end=" ")
        for tranzitie in drum:
            print(f"({tranzitie[0]}, {tranzitie[1]})", end=" ")
        print()
        return True
    else:
        return False

with open("fisier.txt", "r") as f:
    stari = set(f.readline().strip().split())
    stareinitiala=f.readline().strip()
    simboluri = set(f.readline().strip().split())
    stari_finale = set(f.readline().strip().split())
    tranzitii = {}
    for linie in f:
        stare1, caracter, stare2 = linie.strip().split()
        tranzitii[(stare1, caracter)] = stare2
cuvant = input("Introduceti cuvantul: ")
if not verificare_cuvant(tranzitii, stareinitiala, stari_finale, cuvant):
    print("Cuvantul nu este acceptat de automat.")