import asyncio

async def main():
    print('Olá ...')
    await asyncio.sleep(1)
    print('... Mundo!')

asyncio.run(main())