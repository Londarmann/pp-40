from fastapi import FastAPI
from routes import courses

app = FastAPI(title="fastapi crud project")
app.include_router(courses.router)
