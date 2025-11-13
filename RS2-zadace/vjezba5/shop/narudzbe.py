from shop.proizvodi import skladiste

class Narudzba:
    def __init__(self, naruceni_proizvodi, ukupna_cijena):
        self.naruceni_proizvodi = naruceni_proizvodi
        self.ukupna_cijena = ukupna_cijena

    def ispis_narudzbe(self):
        proizvodi_str = ", ".join(
            [f"{p['naziv']} x {p['narucena_kolicina']}" for p in self.naruceni_proizvodi]
        )
        print(f"Naruceni proizvodi: {proizvodi_str}, Ukupna cijena: {self.ukupna_cijena} EUR")

narudzbe = []

def napravi_narudzbu(naruceni_proizvodi):

    if not isinstance(naruceni_proizvodi, list):
        print("Greska: naruceni_proizvodi mora biti lista.")
        return None
    if not naruceni_proizvodi:
        print("Greska: Lista narucenih proizvoda ne smije biti prazna.")
        return None
    for p in naruceni_proizvodi:
        if not isinstance(p, dict):
            print("Greska: Svaki element mora biti rjecnik.")
            return None
        if not all(k in p for k in ("naziv", "cijena", "narucena_kolicina")):
            print("Greska: Svaki proizvod mora imati kljuceve 'naziv', 'cijena' i 'narucena_kolicina'.")
            return None

    for p in naruceni_proizvodi:
        pronadjen = next((s for s in skladiste if s.naziv == p["naziv"]), None)
        if not pronadjen or pronadjen.dostupna_kolicina < p["narucena_kolicina"]:
            print(f"Proizvod {p['naziv']} nije dostupan!")
            return None

    for p in naruceni_proizvodi:
        for s in skladiste:
            if s.naziv == p["naziv"]:
                s.dostupna_kolicina -= p["narucena_kolicina"]

    ukupna_cijena = sum(p["cijena"] * p["narucena_kolicina"] for p in naruceni_proizvodi)

    nova = Narudzba(naruceni_proizvodi, ukupna_cijena)
    narudzbe.append(nova)
    return nova