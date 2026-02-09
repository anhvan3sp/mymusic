from fastapi import FastAPI
from app.database import SessionLocal
from sqlalchemy import text
from routers import songs

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="MyMusic API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # cho phép mọi web gọi (dùng cho học tập)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



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

