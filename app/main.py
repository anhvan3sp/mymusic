from fastapi import FastAPI
from app.database import SessionLocal
from sqlalchemy import text
from routers import songs
app = FastAPI(title="MyMusic API")


@app.get("/test-db")
def test_db():
    db = SessionLocal()
    rows = db.execute(text("SELECT mid, ten_bn FROM ban_nhac")).fetchall()
    db.close()
    return [dict(row._mapping) for row in rows]
app.include_router(songs.router)
   

@app.get("/")
def root():
    return {
        "message": "MyMusic API is running",
        "docs": "/docs"
    }

