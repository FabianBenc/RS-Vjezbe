def suma_parnih():
    suma = 0

    for i in range (1,101):
        if i % 2 == 0:
            suma += i

    print(suma)

    suma = 0
    i = 1
    while i <= 100:
        if i % 2 == 0:
            suma += i
        i += 1
    print(suma)

def neparni_obrnuti():
    for i in range (19, 0, -2):
        print (i, end= " ")
    print()
    
    i = 19
    while i >= 1:
        print(i, end = " ")
        i -= 2
    print()

def fibonacci():
    a = 0
    b = 1

    for _ in range(1000):
        if a > 1000:
            break
        print(a, end = " ")
        a, b = b, a + b
    print()

    a = 0
    b = 1

    while a <= 1000:
        print(a, end = " ")
        a, b = b, a + b
    print()

while True:
    izbor = input("Unesi svoj izbor: ")

    if izbor == "1":
        suma_parnih()
    elif izbor == "2":
        neparni_obrnuti()
    elif izbor == "3":
        fibonacci()
    elif izbor == "0":
        print("Izlaz")
        break
    else:
        print("Ponovi")