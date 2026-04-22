from django.urls import path
from .views import TestAPI, JobListAPI, JobCreateAPI

urlpatterns = [
    path('test/', TestAPI.as_view()),
    path('jobs/', JobListAPI.as_view()),
    path('jobs/create/', JobCreateAPI.as_view()),
]