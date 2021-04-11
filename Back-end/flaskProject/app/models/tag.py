import json
from sqlalchemy import Integer, String, Boolean, Column,ForeignKey
from app.models.base import db, Base


class Tag(Base):
    __tablename__ = 'tag'
    id_tag = Column(Integer,primary_key=True)
    tag = Column(String(64))
    id_good = Column(Integer,ForeignKey('good.id_good'))

    @staticmethod
    def add_one_record(tag,id):
        with db.auto_commit():
            Tag_new = Tag()
            Tag_new.tag = tag
            Tag_new.id_good = id
            db.session.add(Tag_new)
