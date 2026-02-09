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
@router.get("/search")
def search_song(name: str, db: Session = Depends(get_db)):
    songs = (
        db.query(BanNhac)
        .filter(BanNhac.ten_bn.ilike(f"%{name}%"))
        .all()
    )

    result = []
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
@router.get("/by-ca-si")
def get_song_by_ca_si(name: str, db: Session = Depends(get_db)):
    songs = (
        db.query(BanNhac)
        .join(BanThuAm, BanNhac.mid == BanThuAm.mid)
        .join(CaSi, CaSi.sid == BanThuAm.sid)
        .filter(CaSi.ten_cs.ilike(f"%{name}%"))
        .all()
    )

    result = []
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
@router.get("/by-nhac-si")
def get_song_by_nhac_si(name: str, db: Session = Depends(get_db)):
    songs = (
        db.query(BanNhac)
        .join(NhacSi, BanNhac.aid == NhacSi.aid)
        .filter(NhacSi.ten_ns.ilike(f"%{name}%"))
        .all()
    )

    result = []
    for s in songs:
        cas = (
            db.query(CaSi.ten_cs)
            .join(BanThuAm, CaSi.sid == BanThuAm.sid)
            .filter(BanThuAm.mid == s.mid)
            .all()
        )

        result.append({
            "mid": s.mid,
            "ten_bn": s.ten_bn,
            "nhac_si": name,
            "ca_si": [c[0] for c in cas],
            "file_nhac": s.file_nhac
        })

    return result
@router.get("/{mid}")
def get_song_detail(mid: str, db: Session = Depends(get_db)):
    s = db.query(BanNhac).filter(BanNhac.mid == mid).first()
    if not s:
        return {"error": "Song not found"}

    ns = db.query(NhacSi).filter(NhacSi.aid == s.aid).first()
    cas = (
        db.query(CaSi.ten_cs)
        .join(BanThuAm, CaSi.sid == BanThuAm.sid)
        .filter(BanThuAm.mid == s.mid)
        .all()
    )

    return {
        "mid": s.mid,
        "ten_bn": s.ten_bn,
        "nhac_si": ns.ten_ns if ns else "",
        "ca_si": [c[0] for c in cas],
        "file_nhac": s.file_nhac
    }

