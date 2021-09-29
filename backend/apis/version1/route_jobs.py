from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.session import get_db
from db.models.jobs import Job
from schemas.jobs import JobCreate, ShowJob
from db.repository.jobs import create_new_job, retreived_job, list_jobs, update_job_by_id, delete_job_by_id

router = APIRouter()


@router.post("/", response_model=ShowJob)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    owner_id = 8
    job = create_new_job(job=job, db=db, owner_id=owner_id)
    return job


@router.get("/{id}", response_model=ShowJob)
def retreive_job_by_id(id: int, db: Session = Depends(get_db)):
    job = retreived_job(id=id, db=db)
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Job with id {id} does not exist")
    return job


@router.get("", response_model=List[ShowJob])
def retreive_all_jobs(db: Session = Depends(get_db)):
    jobs = list_jobs(db=db)
    return jobs


@router.put("/{id}")
def put_job(id: int, job: JobCreate, db: Session = Depends(get_db)):
    owner_id = 8
    value = update_job_by_id(id, job, db, owner_id)
    if not value:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Job with id {id} does not exist")
    return {"message": "Job updated with sucess"}


@router.delete("/{id}")
def delete_job(id: int, db: Session = Depends(get_db)):
    owner_id = 8
    value = delete_job_by_id(id, db, owner_id)
    if not value:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Job with id {id} does not exist")
    return {"message": "Deleted with sucess!"}
