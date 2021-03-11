from .models import SongSchema
from ..db import songs,database

async def create_song(payload:SongSchema):
    query = songs.insert().values(id=payload.id,name=payload.name,duration=payload.duration,uploaded_time=payload.uploaded_time)
    return await database.execute(query=query)

async def get_all_songs():
    query = songs.select()
    return await database.fetch_all(query=query)