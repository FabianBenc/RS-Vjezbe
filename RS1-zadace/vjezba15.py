def count_vowels_consonants(tekst):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    rezultat = {'vowels': 0, 'consonants': 0}
    
    for znak in tekst:
        if znak in vowels:
            rezultat['vowels'] += 1
        elif znak in consonants:
            rezultat['consonants'] += 1
    
    return rezultat

tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
print(count_vowels_consonants(tekst))