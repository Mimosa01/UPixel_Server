from sqlalchemy import Column, Integer, String, ForeignKey, Table, MetaData
from src.auth.models import user


metadata = MetaData()

user_pictures = Table(
    "user_pictures",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("path", String, nullable=False),
    Column("user_id", Integer, ForeignKey(user.c.id))
)
