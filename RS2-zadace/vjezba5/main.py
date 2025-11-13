from shop import proizvodi, narudzbe

proizvodi_za_dodavanje = [
    {"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
    {"naziv": "Mis", "cijena": 100, "dostupna_kolicina": 100}
]

for p in proizvodi_za_dodavanje:
    proizvodi.dodaj_proizvod(p["naziv"], p["cijena"], p["dostupna_kolicina"])

print("\nSTANJE SKLADISTA")
for p in proizvodi.skladiste:
    p.ispis()

narudzba1 = narudzbe.napravi_narudzbu([
    {"naziv": "Laptop", "cijena": 5000, "narucena_kolicina": 2},
    {"naziv": "Mis", "cijena": 100, "narucena_kolicina": 3}
])

print("\nNARUDZBE")
if narudzba1:
    narudzba1.ispis_narudzbe()

print("\nSTANJE SKLADISTA NAKON NARUDZBE")
for p in proizvodi.skladiste:
    p.ispis()