from typing import List
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from sqlmodel import Session, select
from pamps.db import ActiveSession
from pamps.models.like import Like

router = APIRouter()

    
