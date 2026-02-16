from fastapi import FastAPI

from app.api import users

app = FastAPI(title="Everleaf Backend")

app.include_router(users.router)


@app.get("/")
async def root():
    return {"message": "Everleaf API is running!"}
