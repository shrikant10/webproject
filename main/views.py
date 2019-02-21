from django.shortcuts import render
from .models import Tutorial
from django.http import HttpResponse

# Create your views here.


def homepage(request):
    # return HttpResponse("Hello this is <strong> Homepage</strong>.")
    return render(request=request, template_name="main/home.html", context={"tutorials": Tutorial.objects.all})


