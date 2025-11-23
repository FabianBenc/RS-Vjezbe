import asyncio

async def fetch_users():
    await asyncio.sleep(3)
    return [
        {"id": 1, "ime": "Ana"},
        {"id": 2, "ime": "Marko"}
    ]

async def fetch_products():
    await asyncio.sleep(5)
    return [
        {"id": 10, "proizvod": "Laptop"},
        {"id": 11, "proizvod": "Monitor"}
    ]

async def main():
    users_data, products_data = await asyncio.gather(
        fetch_users(),
        fetch_products()
    )

    print("Korisnici:", users_data)
    print("Proizvodi:", products_data)

asyncio.run(main())