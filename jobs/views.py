from django.shortcuts import render
from .models import jobs


def home(request):
    Jobs= jobs.objects
    return render(request, 'jobs/home.html', {'jobs':Jobs} )
