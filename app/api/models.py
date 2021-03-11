from pydantic import BaseModel,PositiveInt
from enum import Enum
from datetime import datetime
from typing import List,NewType


class AudioTypeSchema(str, Enum):
    """
    #https://fastapi.tiangolo.com/tutorial/path-params/
    """
    song = "song"
    podcast = "podcast"
    audiobook = "audiobook"
'''
Id = NewType("Id",int)
'''
class SongSchema(BaseModel):
    id: int
    name: str
    duration: int
    uploaded_time: datetime

class SongDB(SongSchema):
    id: int
'''    

class PodcastSchema(BaseModel):
    id: Id(...)
    name: str
    duration: int
    uploaded_time: datetime
    host: str
    participants: List[str]

    @validator('participants',each_item=False)
    def check_length(cls,v):
        assert len(v) < 10, f'maximum of 10 participants allowed'
        return v

    @validator('participants',each_item=True)
    def check_length(cls,v):
        assert len(v) < 100, f'maximum of 100 characters allowed'
        return v

class AudioBookSchema(BaseModel):
    id: Id(...)
    title: str(..., max_length=100)
    author: str(..., max_length=100)
    narrator: str(..., max_length=100)
    duration: int
    uploaded_time: datetime
    
'''