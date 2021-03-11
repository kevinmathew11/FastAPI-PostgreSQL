from typing import List
from .crud import create_song,get_all_songs
from .models import SongSchema,SongDB
from fastapi import APIRouter,HTTPException,Path

router = APIRouter()

@router.get("/", response_model=List[SongDB])
async def read_all_songs():
    return await get_all_songs()


@router.post("/",response_model=SongDB,status_code=201)
async def create_song(payload: SongSchema):
    song_id = await create_song(payload)
    response_object = {
        "id": song_id,
        "name": payload.name,
        "duration": payload.duration,
        "uploaded_time": payload.uploaded_time
    }

    return response_object

