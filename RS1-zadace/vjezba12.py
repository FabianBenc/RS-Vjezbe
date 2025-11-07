def obrni_rjecnik(rjecnik):
    novi_rjecnik = {}
    for ključ, vrijednost in rjecnik.items():
        novi_rjecnik[vrijednost] = ključ
    return novi_rjecnik

rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}
print(obrni_rjecnik(rjecnik))