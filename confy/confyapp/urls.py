from django.urls import path
from .views import *

app_name = "confy"
"""
URLS: 
o To create/edit a conference -> POST /api/v1/conference
o To add/edit a talk -> POST /api/v1/talks
o To add/remove speaker/participant from a talk. -> POST /api/v1/attendees for adding, DELETE /api/v1/attendees/<id> for removing
o To list talks in a conference -> GET /api/v1/conferences/<conference_id>/talks
o To list conferences -> GET /api/v1/conferences
"""
urlpatterns = [
    path('api/v1/conferences/', ConferenceApiView.as_view()),
    path('api/v1/conferences/<int:id>', ConferenceApiView.as_view()),
    path('api/v1/talks/', TalkApiView.as_view()),
    path('api/v1/talks/<int:id>', TalkApiView.as_view()),
    path('api/v1/people/', PersonApiView.as_view()),
    path('api/v1/people/<int:id>', PersonApiView.as_view()),
    path('api/v1/attendees/', AttendeeApiView.as_view()),
    path('api/v1/attendees/<int:id>', AttendeeApiView.as_view()),
    path('api/v1/conferences/<int:id>/talks', ConferenceTalksApiView.as_view()),
    path('api/v1/talks/<int:id>/attendees', TalksAttendeesApiView.as_view()),
    path('api/v1/people/<int:id>/talks', PersonTalksApiView.as_view()),
]
