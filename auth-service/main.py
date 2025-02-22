from fastapi import FastAPI
from fastapi.params import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result

from config.database import db_helper
from config.settings import Settings
from config.test_models import Task

app = FastAPI()


@app.get("/")
async def root(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    settings = Settings()
    stmt = select(Task)
    result: Result = await session.execute(stmt)
    tasks = result.scalars().all()

    return tasks
