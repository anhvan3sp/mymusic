from sqlalchemy import Column, String, Integer, ForeignKey
from app.database import Base


class NhacSi(Base):
    __tablename__ = "nhac_si"
    aid = Column(Integer, primary_key=True)
    ten_ns = Column(String(100))

class CaSi(Base):
    __tablename__ = "ca_si"
    sid = Column(String(2), primary_key=True)
    ten_cs = Column(String(100))

class BanNhac(Base):
    __tablename__ = "ban_nhac"
    mid = Column(String(4), primary_key=True)
    aid = Column(Integer, ForeignKey("nhac_si.aid"))
    ten_bn = Column(String(200))
    file_nhac = Column(String(300))

class BanThuAm(Base):
    __tablename__ = "ban_thu_am"
    mid = Column(String(4), ForeignKey("ban_nhac.mid"), primary_key=True)
    sid = Column(String(2), ForeignKey("ca_si.sid"), primary_key=True)
