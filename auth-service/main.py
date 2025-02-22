from fastapi import FastAPI

from config.settings import Settings

app = FastAPI()

@app.get("/")
async def root():
    settings = Settings()

    return {"message": settings.TOKEN}
