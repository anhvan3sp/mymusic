from pydantic import BaseModel

class SongOut(BaseModel):
    mid: str
    ten_bn: str
    nhac_si: str
    ca_si: list[str]
    file_nhac: str
