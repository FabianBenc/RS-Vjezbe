a = float(input("Unesite 1. broj: "))
b = float(input("Unesite 2. broj: "))
c = input("unesite operator: '+','-','*' ili '/': ")

if c == "+":
    rezultat = a + b
    print(f"Rezultat operacije {a} + {b} je {rezultat}")

elif c == "-":
    rezultat = a - b
    print(f"Rezultat operacije {a} - {b} je {rezultat}")

elif c == "*":
    rezultat = a * b
    print(f"Rezultat operacije {a} * {b} je {rezultat}")

elif c == "/":
    if b == 0:
        print ("Dijeljenje s nulom nije dozvoljeno!")

    else:
        rezultat = a / b
        print(f"Rezultat operacije {a} / {b} je {rezultat}")

else:
    print("Nepodrzani operator!")