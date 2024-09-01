
from django.shortcuts import redirect, render
from .forms import StudentForm
from app.models import Student
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User




# Create your views here.
def home(req):
    student=Student.objects.all()
    return render (req,'home.html',{'student':student})


def read(req):
    student=Student.objects.filter(user=req.user)
    #return render(request,template,context) context is always dictionary
    return render(req,'data.html',{'students':student})


@login_required()
def remove(req,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect('/read/')

@login_required()
def create(req):
    if req.method=="POST":
        form=StudentForm(req.POST,req.FILES)

        if form.is_valid():

            Student=form.save(commit=False)
            Student.user=req.user
            Student.save()
            return redirect('/read/')
    else:
        form=StudentForm()
    return render(req,'create.html',{'form':form})

@login_required()
def edit(req,id):
    student=Student.objects.get(id=id)
    if req.method=="POST":
        form=StudentForm(req.POST,req.FILES,instance=student)
        if form.is_valid():
            form.save()
            return redirect('/read/')
    else:
        form=StudentForm(instance=student)
    return render(req,'edit.html',{'form':form})


def loginn(req):
    if req.method=="POST":
        username=req.POST.get("username")
        password=req.POST.get("password")
        user=authenticate(req,username=username,password=password)
        if user is not None:
            login(req,user)
            return redirect('/home/')
    return render (req,'login.html')# type: ignore


def logoutt(req):
    logout(req)
    return redirect('/login/')

def registerr(req):
    if req.method=="POST":
        username=req.POST.get('username')
        password=req.POST.get('password')
        email=req.POST.get('email')
        User.objects.create_user(username=username,password=password,email=email)
        return redirect('/login/')

    return render (req,'register.html')

def about(req):
    return render(req,'about.html')

def contact(req):
    return render(req,'contact.html')


