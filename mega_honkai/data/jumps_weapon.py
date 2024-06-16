import sqlalchemy
from sqlalchemy import orm
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase

class Jump_weapon(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = "jumps_weapon"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey("users.id"))
    item_id = sqlalchemy.Column(sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey("items.id"))
    item_time = sqlalchemy.Column(sqlalchemy.DateTime)

    num_jump = sqlalchemy.Column(sqlalchemy.Integer, default=0)

    garant = sqlalchemy.Column(sqlalchemy.Integer)

    item = orm.relationship('Item')
    user = orm.relationship('User')

    def __repr__(self) -> str:
        return f"<Jump> {self.id}, <user> {self.user.id}, <item> {self.item.id} {self.item.name}"