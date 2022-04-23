from datetime import datetime
from typing import List

import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import aliased, declarative_base, sessionmaker
from sqlalchemy.sql import exists

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/postgres')
Base = declarative_base()

Session = sessionmaker(bind=engine)


class Whitelist(Base):
    __tablename__ = 'whitelist'

    uid = sa.Column(postgresql.ARRAY(sa.Integer), nullable=False, primary_key=True)


class Login(Base):
    __tablename__ = 'logins'

    id = sa.Column(sa.Integer, primary_key=True)
    uid = sa.Column(postgresql.ARRAY(sa.Integer), nullable=False)
    created_at = sa.Column(sa.DateTime, default=datetime.now)


def get_logins_statistic():
    with Session() as session:
        recs = session.query(Login, exists().where(Login.uid == Whitelist.uid)).all()

    recs = [
        {
            'uid': rec[0].uid,
            'created_at': rec[0].created_at.strftime('%d-%m-%Y %S:%M:%H'),
            'has_access': rec[1],
        }
        for rec in recs
    ]

    return recs
