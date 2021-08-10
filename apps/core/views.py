from typing import Dict

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render

from apps.employee.models import Employee


@login_required
def home(request: HttpRequest) -> HttpResponse:
    # data: Dict[str, User]
    # data['user'] = request.user
    # print(request.user)
    return render(request, 'core/index.html')
