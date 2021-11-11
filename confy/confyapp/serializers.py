import ipdb
from rest_framework import serializers
from sqlalchemy.exc import SQLAlchemyError

from confyapp.exceptions import NoRecordFoundException, CantScheduleException, AlreadyRegisteredException, \
    CantUpdateFieldException
from confyapp.models import *
from confyapp.utils import *


class BaseSerializer:
    class Meta:
        model = None
        session = session()
        fields = '__all__'
        update_allowed_fields = ()

    def __init__(self, data=None, many=False):
        result = dict()
        result['data'] = None
        if data:
            if many:
                result['data'] = list()
                for item in data:
                    result['data'].append(item.as_dict())
            else:
                result['data'] = data.as_dict()
        self.__setattr__('data', result['data'])

    def get_queryset(self):
        return self.Meta.session.query(self.Meta.model).all()

    def validate_data(self, data=dict(), entry=None):
        return data

    def filter_by_id(self, idx):
        entry = self.Meta.session.query(self.Meta.model).get(idx)
        if entry is None:
            raise NoRecordFoundException
        return entry

    def perform_operation(self, function=None, params=None):
        bound_session = self.Meta.session.object_session(params['instance'])
        if bound_session is None:
            bound_session = self.Meta.session
        try:
            if function:
                getattr(bound_session, function)(**params)
            bound_session.commit()
        except Exception:
            bound_session.rollback()
            raise

    def create(self, data):
        validated_data = self.validate_data(data)
        entry = self.Meta.model(**validated_data)
        self.perform_operation('add', {'instance': entry})
        self.__setattr__('data', entry.as_dict())

    def update(self, entry, data):
        validated_data = self.validate_data(data, entry)
        for k, v in validated_data.items():
            if k not in self.Meta.update_allowed_fields:
                raise CantUpdateFieldException(params=(k,))
            if hasattr(entry, k):
                setattr(entry, k, v)
        self.perform_operation(params={'instance': entry})
        self.__setattr__('data', entry.as_dict())

    def delete(self, entry):
        try:
            self.perform_operation('delete', {'instance': entry})
            self.__setattr__('data', True)
        except SQLAlchemyError:
            self.__setattr__('data', False)


class PersonSerializer(BaseSerializer):
    class Meta:
        model = Person
        session = session()
        fields = '__all__'
        update_allowed_fields = ('first_name', 'last_name', 'username', 'email')


class ConferenceSerializer(BaseSerializer):
    class Meta:
        model = Conference
        session = session()
        fields = '__all__'
        update_allowed_fields = ('title', 'description', 'start_date', 'end_date')


class TalkSerializer(BaseSerializer):
    class Meta:
        model = Talk
        session = session()
        fields = '__all__'
        update_allowed_fields = ('title', 'description', 'duration', 'start_date', 'end_date')

    def verify_creation(self, conference_id, talk):
        # ipdb.set_trace()
        conference = Conference.query.get(conference_id)
        if conference is None:
            raise NoRecordFoundException(params=("conference"))
        talks = self.Meta.session.query(Talk).filter_by(conference_id=conference_id).order_by(Talk.start_date).all()
        idx = talk['id'] if 'id' in talk else None
        start_date = convertStringToDatetime(talk['start_date'])
        if 'end_date' not in talk:
            if 'duration' not in talk:
                raise ApiException("Should provide at least end_date or duration")
            end_date = (start_date + timedelta(minutes=talk['duration']))
            talk['end_date'] = convertDatetimeToString(end_date)
        else:
            end_date = convertStringToDatetime(talk['end_date'])
        if not (conference.end_date >= end_date and start_date >= conference.start_date):
            raise CantScheduleException(params=(
                "as conference of id {} start_date {}, end_date {}".format(conference.id, conference.start_date,
                                                                                        conference.end_date)))

        for italk in talks:
            val = 0
            if idx and idx != italk.id:
                val = isOverlapping((italk.start_date, italk.end_date), (start_date, end_date))
            if val == 1:
                break
            elif val == -1:
                raise CantScheduleException(params=(
                    "as conflicting with talk_id {} with start_date {}, end_date {}".format(italk.id, italk.start_date,
                                                                                            italk.end_date)))

    def create(self, data):
        self.verify_creation(data['conference_id'], data)
        super().create(data)

    def update(self, entry, data):
        updated_data = entry.as_dict()
        updated_data.update(data)
        self.verify_creation(updated_data['conference_id'], updated_data)
        super().update(entry, data)


class AttendeeSerializer(BaseSerializer):
    class Meta:
        model = Attendee
        session = session()
        fields = '__all__'
        update_allowed_fields = ('role',)

    def verify_creation(self, person_id, event):
        # ipdb.set_trace()
        person = Person.query.get(person_id)
        if person is None:
            raise NoRecordFoundException(params=("person"))
        talk = Talk.query.get(event['talk_id'])
        if talk is None:
            raise NoRecordFoundException(params=("talk"))
        talks = self.Meta.session.query(Talk).join(Attendee).filter(Attendee.person_id == person_id).order_by(
            Talk.start_date).all()
        start_date = talk.start_date
        end_date = talk.end_date
        for italk in talks:
            if talk.id != italk.id:
                val = isOverlapping((italk.start_date, italk.end_date), (start_date, end_date))
            else:
                raise AlreadyRegisteredException()
            if val == 1:
                break
            elif val == -1:
                raise CantScheduleException(params=(
                    "as conflicting with talk_id {} with start_date {}, end_date {}".format(italk.id, italk.start_date,
                                                                                            italk.end_date)))

    def create(self, data):
        self.verify_creation(data['person_id'], data)
        super().create(data)
