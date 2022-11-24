from typing import Optional
from sqlmodel import Field, SQLModel


class Post(SQLModel, table=True):
    """Represents the Post Model"""

    