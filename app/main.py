from fastapi import FastAPI
from .database import Base, engine
from .routers import items

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(items.router)

#Version 6
# Código que se añade
@app.get("/status")
def version():
    return {"status": "Ruiz Quirós, Francisco Javier - v.xx"}
