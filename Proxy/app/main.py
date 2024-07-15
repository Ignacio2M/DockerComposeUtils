from typing import Union
import os
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    prot = os.environ["PORT"]
    return {"Hello": f"World {prot}"}