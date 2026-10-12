from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from typing import List
from database import get_db

import crud
import schemas

router = APIRouter(prefix="/courses", tags=["courses"])


def get_courses_or_404(courses_id: int, db: Session = Depends(get_db)):
    course = crud.get_course(db, courses_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course does not exist")
    return course


@router.post("/", response_model=schemas.CourseRead, status_code=status.HTTP_201_CREATED)
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    return crud.create_course(db, course)


@router.get("/{courses_id}", response_model=schemas.CourseRead)
def get_course(course=Depends(get_courses_or_404)):
    return course


@router.put("/{courses_id}", response_model=schemas.CourseRead)
def replace_course(data: schemas.CourseReplace, course=Depends(get_courses_or_404), db: Session = Depends(get_db)):
    return crud.replace_course(db, course, data)


@router.patch("/{courses_id}", response_model=schemas.CourseRead)
def update_course(data: schemas.CourseUpdate, course=Depends(get_courses_or_404), db: Session = Depends(get_db)):
    return crud.update_course(db, course, data)


@router.delete("/{courses_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_course(course=Depends(get_courses_or_404), db: Session = Depends(get_db)):
    crud.delete_course(db, course)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
