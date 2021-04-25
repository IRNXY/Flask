import sqlalchemy
from .db_session import SqlAlchemyBase


class CorpAnother(SqlAlchemyBase):
    __tablename__ = 'corps_another'
    # news = orm.relation ( "News", back_populates='user' )
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    prize = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    sphere = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    about = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    def __repr__(self):
        return "<User('%s', '%s')>" % (self.name, self.email)
