from sqlalchemy import Column, Table, Integer, String
from src.database import metadata


pictures = Table(
    "pictures",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("path", String)
)
