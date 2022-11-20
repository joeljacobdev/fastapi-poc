from fastapi import APIRouter, Depends
from sqlalchemy.future import select

from app import schemas as app_schemas
from app.database import get_db_session

router = APIRouter()


@router.get("/setup")
async def setup(session=Depends(get_db_session)):
    await session.execute(
        app_schemas.College.__table__.insert(),
        [{"name": f"College {i}"} for i in range(10)],
    )
    result = await session.execute(select(app_schemas.College.id))
    college_ids = result.scalars().all()
    department_batches = []
    for college_id in college_ids:
        department_batches.extend(
            [{"college_id": college_id, "batch": batch} for batch in range(2010, 2023)]
        )
    await session.execute(
        app_schemas.DepartmentBatch.__table__.insert(),
        department_batches,
    )
    result = await session.execute(select(app_schemas.DepartmentBatch.id))
    department_batch_ids = result.scalars().all()
    courses = []
    for dept_batch_id in department_batch_ids:
        courses.extend(
            [
                {"name": f"Course {i}", "department_batch_id": dept_batch_id}
                for i in range(2)
            ]
        )
    await session.execute(
        app_schemas.Course.__table__.insert(),
        courses,
    )
    result = await session.execute(select(app_schemas.Course.id))
    course_ids = result.scalars().all()
    students = [app_schemas.Student(name=f"Student {i}") for i in range(100)]
    session.add_all(students)
    return []
