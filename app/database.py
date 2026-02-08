from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

import os



DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL chưa được cấu hình")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,   # kiểm tra connection trước khi dùng
    pool_recycle=300,     # recycle connection sau 5 phút
)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
