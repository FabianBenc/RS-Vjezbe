import asyncio

async def secure_data(data):
    await asyncio.sleep(3)
    return {
        'prezime': data['prezime'],
        'broj_kartice': hash(str(data['broj_kartice'])),
        'CVV': hash(str(data['CVV']))
    }

async def main():
    lista_podataka = [
        {'prezime': 'Horvat', 'broj_kartice': '1111222233334444', 'CVV': '123'},
        {'prezime': 'Kovač',  'broj_kartice': '5555666677778888', 'CVV': '456'},
        {'prezime': 'Barić',  'broj_kartice': '9999000011112222', 'CVV': '789'},
    ]

    zadaci = [
        asyncio.create_task(secure_data(item))
        for item in lista_podataka
    ]

    rezultati = await asyncio.gather(*zadaci)

    for r in rezultati:
        print(r)

asyncio.run(main())