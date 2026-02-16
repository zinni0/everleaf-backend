from fastapi import FastAPI

from app.routes import tasks

app = FastAPI(title="Everleaf Backend")

app.include_router(tasks.router)
