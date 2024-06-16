import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True,
                           autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey("users.id"))
    job = sqlalchemy.Column(sqlalchemy.String)
    work_size = sqlalchemy.Column(sqlalchemy.Float)
    collaborators = sqlalchemy.Column(sqlalchemy.String)
    start_date = sqlalchemy.Column(sqlalchemy.Date)
    end_date = sqlalchemy.Column(sqlalchemy.Date)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean)
    user = orm.relationship('User')

    categories = orm.relationship('Categories',
                                  secondary='link',
                                  overlaps="categories",
                                  single_parent=True,
                                  cascade="all, delete, delete-orphan")

    def __repr__(self) -> str:
        return f"<Job> {self.job}"


class Categories(SqlAlchemyBase):
    __tablename__ = 'categories'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True,
                           autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String)

    jobs = orm.relationship("Jobs",
                            secondary='link',
                            overlaps="categories",
                            backref=orm.backref("jobs", lazy="dynamic"),
                            single_parent=True,
                            cascade="all, delete, delete-orphan")

    def __repr__(self) -> str:
        return f"<Categories> {self.title}"


class Link(SqlAlchemyBase):
    __tablename__ = 'link'
    categories_id = sqlalchemy.Column(sqlalchemy.Integer,
                                      sqlalchemy.ForeignKey('categories.id'),
                                      primary_key=True)

    jobs_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey('jobs.id'),
                                primary_key=True)