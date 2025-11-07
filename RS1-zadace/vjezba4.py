zbroj = 0

while True:
    broj = int(input("Unesi neki broj: "))

    if broj == 0:
        break
    
    zbroj += broj

print(f"Zbroj unesenih brojeva je {zbroj}")