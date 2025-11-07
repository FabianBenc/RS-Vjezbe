def provjera_lozinke(lozinka):

    if len(lozinka) < 8 or len(lozinka) > 15:
        print("Lozinka mora sadržavati između 8 i 15 znakova")
        return False

    veliko = False
    broj = False
    for znak in lozinka:
        if znak.isupper():
            veliko = True
        if znak.isdigit():
            broj = True

        lozinka_lower = lozinka.lower()
    if "password" in lozinka_lower or "lozinka" in lozinka_lower:
        print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'")
        return False
    
    if not (veliko and broj):
        print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj")
        return False

    print("Lozinka je jaka!")
    return True

lozinka = input("Unesite lozinku: ")
provjera_lozinke(lozinka)