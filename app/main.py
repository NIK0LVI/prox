import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from app.db.database import Base, engine
from app.offices.routes import office_router
from app.employees.routes import employee_router
from app.students.routes import student_router

Base.metadata.create_all(bind=engine)


def init_app():
    app = FastAPI()
    app.include_router(office_router)
    app.include_router(employee_router)
    app.include_router(student_router)

    return app


app = init_app()


@app.get("/", include_in_schema=False)
def hello_world():
    return RedirectResponse("/docs")


if __name__ == "__main__":
    uvicorn.run(app)
