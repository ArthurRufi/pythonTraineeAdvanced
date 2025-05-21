from enum import Enum
import asyncio

class EsperaResposta(Enum):
    CONFIRMADO = 200
    RECUSADO = 401

async def respostas(response):
    if EsperaResposta.CONFIRMADO.value == response:
        return "OK"
    elif EsperaResposta.RECUSADO.value == response:
        return "NEGATIVE"
    else:
        return "Not available"

# Executa corretamente a função async
async def main():
    print(await respostas(200))
    print(await respostas(401))
    print(await respostas(299))

asyncio.run(main())
