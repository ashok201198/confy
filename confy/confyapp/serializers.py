import ipdb
from rest_framework import serializers
from sqlalchemy.exc import SQLAlchemyError

from confyapp.exceptions import NoRecordFoundException
from confyapp.models import *


class BaseSerializer:
    class Meta:
        model = None
        session = session()
        fields = '__all__'

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
            ipdb.set_trace()
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


class ConferenceSerializer(BaseSerializer):
    class Meta:
        model = Conference
        session = session()
        fields = '__all__'

    # def validate_data(self, data, entry=None):
    #     prefilled = dict()
    #     if entry:
    #         prefilled = entry.as_dict()
    #     if 'start_date' in


class TalkSerializer(BaseSerializer):
    class Meta:
        model = Talk
        session = session()
        fields = '__all__'


class AttendeeSerializer(BaseSerializer):
    class Meta:
        model = Attendee
        session = session()
        fields = '__all__'
