from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base_class import Base
import uvicorn


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, varion=settings.PROJECT_VERSION)
    create_tables()
    return app


app = start_application()


@app.get("/")
def hello_api():
    return {"message": "Hello World!"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
