import enum
from datetime import datetime, timedelta

import sqlalchemy.event
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.sql import func
from confyapp.base import Base, session
from confyapp.listeners import *


class Role(str, enum.Enum):
    Participant = 'Participant'
    Speaker = 'Speaker'


class Attendee(Base):
    __tablename__ = 'attendees'
    id = Column(Integer, primary_key=True, autoincrement=True)
    talk_id = Column('talk_id', Integer, ForeignKey('talks.id', ondelete='CASCADE'), nullable=False)
    person_id = Column('person_id', Integer, ForeignKey('people.id', ondelete='CASCADE'), nullable=False)
    role = Column(Enum(Role), default=Role.Participant)
    created_at = Column('created_at', DateTime, server_default=func.now())
    updated_at = Column('updated_at', DateTime, server_default=func.now(), onupdate=func.now())

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(40), default='')
    lastname = Column(String(40), default='')
    username = Column(String(40), nullable=False, unique=True)
    email = Column(String(40), nullable=False, unique=True)
    created_at = Column('created_at', DateTime, server_default=func.now())
    updated_at = Column('updated_at', DateTime, server_default=func.now(), onupdate=func.now())
    attendee = relationship(Attendee, backref="Person", passive_deletes='all')

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Talk(Base):
    __tablename__ = 'talks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(40), default='')
    description = Column(String(400), default='')
    duration = Column(Integer, default=1)
    start_date = Column('start_date', DateTime, server_default=func.now())
    end_date = Column('end_date', DateTime, server_default=func.now())
    conference_id = Column('conference_id', Integer, ForeignKey('conferences.id', ondelete='CASCADE'), nullable=False)
    created_at = Column('created_at', DateTime, server_default=func.now())
    updated_at = Column('updated_at', DateTime, server_default=func.now(), onupdate=func.now())
    attendee = relationship(Attendee, backref="Talk", passive_deletes='all')

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @validates('start_date', 'end_date')
    def validate_dates(self, key, field):
        if key == 'end_date' and isinstance(self.start_date, datetime):
            if self.start_date > field:
                raise AssertionError("The end_date field must be greater-or-equal than the start_date field")
        return field

    @validates('duration')
    def validate_duration(self, key, field):
        if field <= 0:
            raise AssertionError("The talk time should be greater that 0 minutes")
        return field


sqlalchemy.event.listen(Talk, 'before_insert', before_talk_insert_or_update)
sqlalchemy.event.listen(Talk, 'before_update', before_talk_insert_or_update)


class Conference(Base):
    __tablename__ = 'conferences'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(40), default='')
    description = Column(String(400), default='')
    start_date = Column('start_date', DateTime, server_default=func.now())
    end_date = Column('end_date', DateTime, server_default=func.now())
    created_at = Column('created_at', DateTime, server_default=func.now())
    updated_at = Column('updated_at', DateTime, server_default=func.now(), onupdate=func.now())
    talks = relationship(Talk, backref="Conference", passive_deletes='all')

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @validates('start_date', 'end_date')
    def validate_dates(self, key, field):
        if key == 'end_date' and isinstance(self.start_date, datetime):
            if self.start_date > field:
                raise AssertionError("The stopped_at field must be greater-or-equal than the start_date field")
        return field


sqlalchemy.event.listen(Conference, 'before_insert', before_conference_insert_or_update)
sqlalchemy.event.listen(Conference, 'before_update', before_conference_insert_or_update)
