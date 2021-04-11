from sqlalchemy import Integer, String, Boolean, Column, Float
from app.models.base import Base, db


class Good(Base):
    __tablename__ = 'good'
    id_good = Column(Integer, primary_key=True)
    name = Column(String(64))
    price = Column(Float)
    count = Column(Integer)
    rel = Column(String(64))
    info = Column(String(255))

    @staticmethod
    def add_good(name,price,count,rel,info):
        with db.auto_commit():
            good = Good()
            good.name = name
            good.price = price
            good.count = count
            good.rel = rel
            good.info = info
            db.session.add(good)
