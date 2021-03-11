import os
from sqlalchemy import (Column,String,DateTime,Integer,MetaData, create_engine, Table)
from sqlalchemy.sql import func

from databases import Database

DATABASE_URL = os.environ.get("DATABASE_URL")

#SQL Alchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()

songs = Table(
    "songs",
    metadata,
    Column("id",Integer,primary_key=True),
    Column("name",String(100)),
    Column("duration",Integer,primary_key=True),
    Column("uploaded_time", DateTime, default=func.now(), nullable=False),
)

#databases query builder
database = Database(DATABASE_URL)
