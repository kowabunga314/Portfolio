from django.shortcuts import render
from .models import Job


# Home
def home(request):

    jobs = Job.objects

    return render(request, 'jobs/home.html', {'jobs': jobs})

