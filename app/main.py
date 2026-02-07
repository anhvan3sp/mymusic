from fastapi import FastAPI
from app.database import SessionLocal
from sqlalchemy import text

app = FastAPI(title="MyMusic API")

@app.get("/test-db")
def test_db():
    db = SessionLocal()
    result = db.execute(text("SELECT mid, ten_bn FROM ban_nhac"))
    data = result.fetchall()
    db.close()
    return data
