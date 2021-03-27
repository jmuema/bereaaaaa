from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Classroom, Unit, Notes,Task
from django.contrib.auth import login, authenticate
from .models import Classroom
from .forms import StudentSignUp
from .decorators import allowed_users
from django.contrib.auth.models import Group
from django.views.generic import CreateView
from .forms import StudentSignUp
from .decorators import unauthenticated_user

# Create your views here.

@login_required
def home_view(request):
    return render(request, 'portal/index.html')


def signup_view(request):
    if request.method == 'POST':
        form = StudentSignUp(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = StudentSignUp()
    return render(request, 'portal/signup.html', {'form': form})
        

@login_required(login_url='/login/')
def classes(request):
    print("-" * 30)
    print("Hello")
    classes= Classroom.objects.all()
    return render(request,'students/index.html',{'classes':classes})
    
    

@login_required(login_url='/login/')
def units(request,un_id):
    unit = Unit.objects.filter(classroom_id=un_id)
    # print([x.classname for x in classes])
    return render(request,'students/units.html',{"unit": unit})

@login_required(login_url='/login/')
@allowed_users(allowed_roles=['comrades'])
def notes(request,not_id):
    notes = Notes.objects.filter(unit_id=not_id)
    return render(request,'students/notes.html',{"notes": notes})

@login_required(login_url='/login/')
@allowed_users(allowed_roles=['comrades'])
def assignments(request,ass_id):
    assignment = Task.objects.filter(unit_id=ass_id)
    print (assignment)
    return render(request,'assignments.html',{"assignment": assignment})
  