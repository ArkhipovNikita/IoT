from datetime import datetime
from typing import List

import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import declarative_base, sessionmaker
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


def has_uid_access(uid: List[int]) -> bool:
    with Session() as session:
        has_access = session.query(exists().where(Whitelist.uid.contains(uid))).scalar()

    return has_access


def create_login(uid: List[int]) -> Login:
    with Session() as session:
        login = Login(uid=uid)
        session.add(login)
        session.commit()

    return login
