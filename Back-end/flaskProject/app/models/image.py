from sqlalchemy import Integer, String, Boolean, Column, Float, ForeignKey
from app.models.base import Base, db

class Image(Base):
    __tablename__ = 'image'
    id_image = Column(Integer,primary_key=True)
    base64 = Column(String(100000))
    id_good = Column(Integer,ForeignKey('good.id_good'))

    @staticmethod
    def add_one_record(base64,id_good):
        with db.auto_commit():
            Image_new = Image()
            Image_new.base64 = base64
            Image_new.id_good = id_good
            db.session.add(Image_new)
