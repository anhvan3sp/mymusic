from fastapi import FastAPI
from routers import songs

app = FastAPI(title="MyMusic API")

app.include_router(songs.router)

