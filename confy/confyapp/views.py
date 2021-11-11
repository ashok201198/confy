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
