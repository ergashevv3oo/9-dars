from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
import uvicorn

from database import engine, Base, get_db
from schemas import DoctorCreate, DoctorResponse
from crud import create_doctor

app = FastAPI()


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.post("/doctor", response_model=DoctorResponse)
async def add_doctor(doctor: DoctorCreate, db: AsyncSession = Depends(get_db)):
    return await create_doctor(doctor, db)

if __name__ == '__main__':
    uvicorn.run(app)