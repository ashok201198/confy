from django.urls import path
from .views import *

app_name = "confy"

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
