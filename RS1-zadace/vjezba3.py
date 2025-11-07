import random

random_br =  random.randint(1,10)
broj_je_pogoden = False
broj_pokusaja = 0

while not broj_je_pogoden:
    a = int(input("Unesi broj izmedu 1 i 100: "))
    broj_pokusaja += 1

    if a == random_br:
        broj_je_pogoden = True
        print(f"Bravo, pogodio si u {broj_pokusaja} pokusaja.")
    elif a > random_br:
        print ("Trazeni broj je manji")
    else:
        print ("Trazeni broj je veci")