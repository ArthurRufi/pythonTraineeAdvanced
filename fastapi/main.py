from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {'messagem aleatoria': "Minha vida"}

@app.get("/low/{item}")
async def room(item: int):
    return {'messagem gravada': item}