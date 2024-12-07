from fastapi import FastAPI

from src.form_check.router import router as form_check_router


app = FastAPI()

app.include_router(form_check_router)