"""35. FastAPI'da yangi endpoint (marshrut) qanday yaratiladi?"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome():
    return "Hi"

# bu yerda endpoint - @app.get("/") hisoblanadi.