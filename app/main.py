from fastapi import FastAPI
from app.database import SessionLocal
from sqlalchemy import text

app = FastAPI(title="MyMusic API")

@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "MyMusic API is running",
        "docs": "/docs",
        "test_db": "/test-db"
    }

@app.get("/test-db")
def test_db():
    db = SessionLocal()
    rows = db.execute(text("SELECT mid, ten_bn FROM ban_nhac")).fetchall()
    db.close()
    return [dict(row._mapping) for row in rows]

