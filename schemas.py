from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict
from decimal import Decimal
from typing import Optional
from enum import Enum


class CourseLevel(str, Enum):
    beginner = "Beginner"
    intermediate = "Intermediate"
    advanced = "Advanced"


class CourseBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(default=None, max_length=300)
    price: Decimal = Field(default=Decimal("0"), ge=0, max_digits=10, decimal_places=2)
    level: CourseLevel = CourseLevel.beginner


class CourseCreate(CourseBase):
    """how we can create course"""


class CourseReplace(CourseBase):
    """how we can replace course"""


class CourseUpdate(BaseModel):
    """how we can update course"""
    title: Optional[str] = Field(default=None, min_length=1, max_length=100)
    description: Optional[str] = Field(default=None, max_length=300)
    price: Optional[Decimal] = Field(default=None, ge=0, max_digits=10, decimal_places=2)
    level: Optional[CourseLevel] = None
    is_active: Optional[bool] = None


class CourseRead(CourseBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime
