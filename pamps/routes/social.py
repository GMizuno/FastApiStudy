from typing import List
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from sqlmodel import Session, select
from pamps.db import ActiveSession
from pamps.auth import AuthenticatedUser
from pamps.models import Social
from pamps.models.user import User

router = APIRouter()
