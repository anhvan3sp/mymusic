from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from urllib.parse import quote_plus


raw_password = os.getenv("DB_PASSWORD")
password = quote_plus(raw_password)

DATABASE_URL = (
    f"mysql+pymysql://avnadmin:{password}"
    f"@mysql-1f784f93-anhvan2sp-e73a.aivencloud.com:17593/mymusic"
)





if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL chưa được cấu hình")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,   # kiểm tra connection trước khi dùng
    pool_recycle=300,     # recycle connection sau 5 phút
)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
