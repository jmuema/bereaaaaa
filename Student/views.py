from django.shortcuts import render
from portal.models import Classroom
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required
def Home(request):
    print("-" * 30)
    print("Hello")
    classes= Classroom.objects.all()
    return render (request, 'students/index.html',{'classes':classes})


