from django.http import HttpResponse
from django.shortcuts import render
from .models import Job


# Home
def home(request):

    jobs = Job.objects

    return render(request, 'jobs/home.html', {'jobs': jobs})


def pdf_view(request):
    with open('static/Frost_Resume.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response

