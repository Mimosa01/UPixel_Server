from sqlalchemy import Column, Integer, String, ForeignKey, Table, MetaData
from src.auth.models import user

metadata = MetaData()

general_colorings = Table(
    'general_colorings',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("path", String, nullable=False)
)

user_colorings = Table(
    "user_colorings",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("path", String, nullable=False),
    Column("user_id", Integer, ForeignKey(user.c.id))
)
