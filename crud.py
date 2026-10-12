from sqlalchemy.orm import Session
from sqlalchemy import select

import models
import schemas


def create_course(db: Session, data: schemas.CourseCreate):
    course = models.Course(**data.model_dump())
    db.add(course)
    db.commit()
    db.refresh(course)
    return course


def get_course(db: Session, course_id: int):
    return db.get(models.Course, course_id)


def replace_course(db: Session, course: models.Course, data: schemas.CourseReplace):
    for field, value in data.model_dump().items():
        setattr(course, field, value)
    db.commit()
    db.refresh(course)
    return course


def update_course(db: Session, course: models.Course, data: schemas.CourseUpdate):
    changes = data.model_dump(exclude_unset=True)
    for field, value in changes.items():
        setattr(course, field, value)
    db.commit()
    db.refresh(course)
    return course


def delete_course(db: Session, course: models.Course):
    db.delete(course)  # hard delete
    db.commit()
