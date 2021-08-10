from django import urls
from django.urls import path

from apps.company.views import CompanyCreateView, CompanyEditView

urlpatterns = [
    path("new", CompanyCreateView.as_view(), name="create_company"),
    path("edit/<int:pk>", CompanyEditView.as_view(), name="edit_company"),
]
