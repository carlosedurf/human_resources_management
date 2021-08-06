from django.urls import path

from apps.employee.views import home

urlpatterns = [
    path("", home),
]
