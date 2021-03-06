#!/usr/bin/env python3
"""
DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from user import Base, User


class DB:
    """ class DB """
    def __init__(self):
        """ Constructor """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """ session """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Add a new user in DB """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """ find a user by a filter """
        data = self._session.query(User).filter_by(**kwargs)
        return data.one()

    def update_user(self, user_id: int, **kwargs) -> None:
        """ locate the user to update """
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if key not in list(user.__dict__.keys()):
                raise ValueError()
            else:
                setattr(user, key, value)
        self._session.add(user)
        self._session.commit()
