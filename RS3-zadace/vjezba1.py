import asyncio

async def fetch_numbers():
    await asyncio.sleep(3)
    numbers = [i for i in range(1, 11)]
    print("Podaci dohvaćeni.")
    return numbers

async def main():
    data = await fetch_numbers()
    print(data)

asyncio.run(main())