import sqlalchemy
from sqlalchemy import orm
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash

from .db_session import SqlAlchemyBase

class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(40), nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String(100))

    count_all_jumps = sqlalchemy.Column(sqlalchemy.String(30))
    count_garant_5 = sqlalchemy.Column(sqlalchemy.String(30))
    count_garant_4 = sqlalchemy.Column(sqlalchemy.String(30))


    hashed_password = sqlalchemy.Column(sqlalchemy.String(200), nullable=True)

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
    
    def __repr__(self) -> str:
        return f"<User> {self.id}, {self.name}"