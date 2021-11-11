from rest_framework import status, views
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import *


class ConferenceApiView(views.APIView):
    serializer = ConferenceSerializer

    def get(self, request, *args, **kwargs):
        many = True
        try:
            if 'id' in kwargs:
                many = False
                query_set = self.serializer().filter_by_id(kwargs['id'])
            else:
                query_set = self.serializer().get_queryset()
            entries = self.serializer(query_set, many=many)
            return JsonResponse(entries.data, safe=False, status=status.HTTP_200_OK)
        except BaseException as e:
            return Response({"Message": str(e.__repr__())}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer()
            serializer.create(request.data)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
        except BaseException as e:
            return Response({"Message": str(e.__repr__())}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        try:
            id = kwargs['id']
            serializer = self.serializer()
            entry = serializer.filter_by_id(id)
            serializer.update(entry, request.data)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
        except BaseException as e:
            return Response({"Message": str(e.__repr__())}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            id = kwargs['id']
            serializer = self.serializer()
            entry = serializer.filter_by_id(id)
            serializer.delete(entry)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
        except BaseException as e:
            return Response({"Message": str(e.__repr__())}, status=status.HTTP_400_BAD_REQUEST)


class TalkApiView(views.APIView):
    serializer = TalkSerializer

    def get(self, request, *args, **kwargs):
        many = True
        try:
            if 'id' in kwargs:
                many = False
                query_set = self.serializer().filter_by_id(kwargs['id'])
            else:
                query_set = self.serializer().get_queryset()
            entries = self.serializer(query_set, many=many)
            return JsonResponse(entries.data, safe=False, status=status.HTTP_200_OK)
        except BaseException as e:
            return Response({"Message": str(e.__repr__())}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer()
            serializer.create(request.data)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
        except BaseException as e:
            return Response({"Message": str(e.__repr__())}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        try:
            id = kwargs['id']
            serializer = self.serializer()
            entry = serializer.filter_by_id(id)
            serializer.update(entry, request.data)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
        except BaseException as e:
            return Response({"Message": str(e.__repr__())}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            id = kwargs['id']
            serializer = self.serializer()
            entry = serializer.filter_by_id(id)
            serializer.delete(entry)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
        except BaseException as e:
            return Response({"Message": str(e.__repr__())}, status=status.HTTP_400_BAD_REQUEST)


class PersonApiView(views.APIView):
    serializer = PersonSerializer

    def get(self, request, *args, **kwargs):
        many = True
        try:
            if 'id' in kwargs:
                many = False
                query_set = self.serializer().filter_by_id(kwargs['id'])
            else:
                query_set = self.serializer().get_queryset()
            entries = self.serializer(query_set, many=many)
            return JsonResponse(entries.data, safe=False, status=status.HTTP_200_OK)
        except BaseException as e:
            return Response({"Message": str(e.__repr__())}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer()
            serializer.create(request.data)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
        except BaseException as e:
            return Response({"Message": str(e.__repr__())}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        try:
            id = kwargs['id']
            serializer = self.serializer()
            entry = serializer.filter_by_id(id)
            serializer.update(entry, request.data)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
        except BaseException as e:
            return Response({"Message": str(e.__repr__())}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            id = kwargs['id']
            serializer = self.serializer()
            entry = serializer.filter_by_id(id)
            serializer.delete(entry)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
        except BaseException as e:
            return Response({"Message": str(e.__repr__())}, status=status.HTTP_400_BAD_REQUEST)


class AttendeeApiView(views.APIView):
    serializer = AttendeeSerializer

    def get(self, request, *args, **kwargs):
        many = True
        try:
            if 'id' in kwargs:
                many = False
                query_set = self.serializer().filter_by_id(kwargs['id'])
            else:
                query_set = self.serializer().get_queryset()
            entries = self.serializer(query_set, many=many)
            return JsonResponse(entries.data, safe=False, status=status.HTTP_200_OK)
        except BaseException as e:
            return Response({"Message": str(e.__repr__())}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer()
            serializer.create(request.data)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
        except BaseException as e:
            return Response({"Message": str(e.__repr__())}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        try:
            id = kwargs['id']
            serializer = self.serializer()
            entry = serializer.filter_by_id(id)
            serializer.update(entry, request.data)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
        except BaseException as e:
            return Response({"Message": str(e.__repr__())}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            id = kwargs['id']
            serializer = self.serializer()
            entry = serializer.filter_by_id(id)
            serializer.delete(entry)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
        except BaseException as e:
            return Response({"Message": str(e.__repr__())}, status=status.HTTP_400_BAD_REQUEST)


class ConferenceTalksApiView(views.APIView):

    def get(self, request, *args, **kwargs):
        conference_id = kwargs['id']
        conference = Conference.query.get(conference_id)
        talks = Talk.query.filter_by(conference_id=conference_id).all()
        result = dict()
        result.update(ConferenceSerializer(conference, many=False).data)
        if talks:
            talks = {"talks": TalkSerializer(talks, many=True).data}
        else:
            talks = {'talks': []}
        result.update(talks)
        return JsonResponse(result, safe=False, status=status.HTTP_200_OK)


class TalksAttendeesApiView(views.APIView):

    def get(self, request, *args, **kwargs):
        talk_id = kwargs['id']
        talk = Talk.query.get(talk_id)
        speakers = Person.query.join(Attendee).filter(Attendee.talk_id==talk_id).filter(
            Attendee.role == Role.Speaker).all()
        participants = Person.query.join(Attendee).filter(Attendee.talk_id==talk_id).filter(
            Attendee.role == Role.Participant).all()
        result = dict()
        result.update(TalkSerializer(talk, many=False).data)
        if speakers:
            speakers = {"speakers": PersonSerializer(speakers, many=True).data}
        else:
            speakers = {'speakers': []}
        result.update(speakers)
        if participants:
            participants = {"participants": PersonSerializer(participants, many=True).data}
        else:
            participants = {'participants': []}
        result.update(participants)
        return JsonResponse(result, safe=False, status=status.HTTP_200_OK)


class PersonTalksApiView(views.APIView):

    def get(self, request, *args, **kwargs):
        person_id = kwargs['id']
        person = Person.query.get(person_id)
        speaks = Talk.query.join(Attendee).filter(Attendee.person_id==person_id).filter(
            Attendee.role == Role.Speaker).all()
        participates = Talk.query.join(Attendee).filter(Attendee.person_id==person_id).filter(
            Attendee.role == Role.Participant).all()
        result = dict()
        result.update(PersonSerializer(person, many=False).data)
        if speaks:
            speakers = {"speaks_in": TalkSerializer(speaks, many=True).data}
        else:
            speakers = {'speaks_in': []}
        result.update(speakers)
        if participates:
            participants = {"listens_in": TalkSerializer(participates, many=True).data}
        else:
            participants = {'listens_in': []}
        result.update(participants)
        return JsonResponse(result, safe=False, status=status.HTTP_200_OK)
