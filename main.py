from fastapi import FastAPI
from app.db import metadata,engine,database
from app.api import songs


app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(songs.router,prefix="/songs",tags=["songs"])