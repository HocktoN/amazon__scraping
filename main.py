from fastapi import FastAPI
from scrap_amazon import getData

app = FastAPI()

@app.get("/")
def main():
    datas = getData()
    return datas
