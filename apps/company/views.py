from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView

from apps.company.models import Company
from apps.employee.models import Employee


class CompanyCreateView(CreateView):
    model = Company
    fields = ['name']

    def form_valid(self, form) -> HttpResponse:
        company: Company = form.save()
        employee: Employee = self.request.user.employee
        employee.company = company
        employee.save()
        return HttpResponse('Ok')

class CompanyEditView(UpdateView):
    model = Company
    fields = ['name']
