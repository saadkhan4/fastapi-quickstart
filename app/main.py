from fastapi import FastAPI
from .routers import users, items

app = FastAPI(
     version="1.0.0",
     title="FastAPI Starter Kit",
     description="This is starter kit for quick start"
)

app.include_router(users.router)
app.include_router(items.router)

@app.get("/")
def root():
     return { "message": "Hello World" }