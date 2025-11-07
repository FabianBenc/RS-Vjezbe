def ukloni_duplikate(lista):
    dupli = set()
    nova_lista = []
    for elem in lista:
        if elem not in dupli:
            nova_lista.append(elem)
            dupli.add(elem)
    return nova_lista

lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(ukloni_duplikate(lista))