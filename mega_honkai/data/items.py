import sqlalchemy
from sqlalchemy import orm
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase

class Item(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = "items"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)

    name = sqlalchemy.Column(sqlalchemy.String(100))
    rank = sqlalchemy.Column(sqlalchemy.Integer)
    type = sqlalchemy.Column(sqlalchemy.String(40))

    def __repr__(self) -> str:
        return f"<Item> {self.id}, {self.name}, {self.rank}, {self.type}"