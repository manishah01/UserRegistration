from django.shortcuts import render, redirect, HttpResponse
from .models import User

def index(request):
    context = {
        "all_users": User.objects.all()
    }
    return render(request, "users.html", context)

def make_new_user(request):
    User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email_address=request.POST['email_address'],
        age=request.POST['age']
    )
    return redirect('/')