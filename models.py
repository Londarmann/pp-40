from sqlalchemy import Column, Integer, String, Numeric, Boolean, DateTime, func
from database import Base


class BaseModel(Base):
    __abstract__ = True


class Course(BaseModel):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(300), nullable=True)
    price = Column(Numeric(10, 2), nullable=False, default=0)
    level = Column(String(20), nullable=False, default='Beginner')
    is_active = Column(Boolean, default=True, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    deleted_at = Column(DateTime(timezone=True), index=True, nullable=True)
