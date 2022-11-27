from datetime import datetime
from typing import Optional, List, TYPE_CHECKING
from sqlmodel import Field, SQLModel,  Relationship
from pamps.security import HashedPassword
from pydantic import BaseModel

if TYPE_CHECKING:
    from pamps.models.post import Post

class User(SQLModel, table=True):
    """Represents the User Model"""
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, nullable=False)
    username: str = Field(unique=True, nullable=False)
    avatar: Optional[str] = None
    bio: Optional[str] = None
    password: HashedPassword

    # it populates the .user attribute on the Post Model
    posts: List["Post"] = Relationship(back_populates='user')


class UserResponse(BaseModel):
    """Serializer for User Response"""
    username: str
    avatar: Optional[str] = None
    bio: Optional[str] = None


class UserRequest(BaseModel):
    """Serializer for User request payload"""
    email: str
    username: str
    password: str
    avatar: Optional[str] = None
    bio: Optional[str] = None


class Social(SQLModel, table=True):
    """Represents the Social Model"""
    id: Optional[int] = Field(default=None, primary_key=True)
    user_from_id: Optional[int] = Field(foreign_key="user.id")
    user_to_id: Optional[int] = Field(foreign_key="user.id")
    date: datetime = Field(default_factory=datetime.utcnow, nullable=False)
