import sqlalchemy
from .db_session import SqlAlchemyBase


class CorpNext(SqlAlchemyBase):
    __tablename__ = 'corps_next'
    # news = orm.relation ( "News", back_populates='user' )
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    prize = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    sphere = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    count = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    age = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    about = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    def __repr__(self):
        return "<CorpNext('%s')>" % (self.prize)
