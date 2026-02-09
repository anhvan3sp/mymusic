from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import BanNhac, NhacSi, CaSi, BanThuAm


router = APIRouter(prefix="/songs", tags=["Songs"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_all_songs(db: Session = Depends(get_db)):
    result = []
    songs = db.query(BanNhac).all()

    for s in songs:
        ns = db.query(NhacSi).filter(NhacSi.aid == s.aid).first()
        cas = (
            db.query(CaSi.ten_cs)
            .join(BanThuAm, CaSi.sid == BanThuAm.sid)
            .filter(BanThuAm.mid == s.mid)
            .all()
        )

        result.append({
            "mid": s.mid,
            "ten_bn": s.ten_bn,
            "nhac_si": ns.ten_ns if ns else "",
            "ca_si": [c[0] for c in cas],
            "file_nhac": s.file_nhac
        })

    return result
