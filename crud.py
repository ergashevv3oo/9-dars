from sqlalchemy.ext.asyncio import AsyncSession

from models import *
from schemas import *

async def create_doctor(doctor: DoctorCreate, db: AsyncSession) -> DoctorResponse:
    db_doctor = Doctor(**doctor.model_dump())
    db.add(db_doctor)
    await db.commit()
    await db.refresh(db_doctor)
    return DoctorResponse.model_validate(db_doctor)
