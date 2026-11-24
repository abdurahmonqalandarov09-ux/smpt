from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from .models import *
from random import randint
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            is_active = False
        )
        user.save()
        code = str(randint(100000, 999999))
        ConfirmEmail.objects.update_or_create(
            user = user,
            code = code
        )
        send_mail(
            "Confirm your email",
            f"Your code: {code}",
            'norep1y@softc1ub.tj',
            [user.email]
        )
        return redirect('confirm_email')
    return render(request, 'registration.html')



def confirm_email(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        code = request.POST.get('code')
        user = request.POST.get('user')
        code_obj = ConfirmEmail.objects.filter(user = user).first()

        if code_obj.code == code:
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('profile.html')
        else:
            return redirect('confirm_email')
        return render(request, 'confirm_email.html')




@login_required
def show_profile(request):
    return render(request, 'profile')


def login_user(request):
    if request.method == 'POST':
        data = request.POST
        user = authenticate(request, username = data['username'], password = data['password'])
        if user is not None:
            login(request, user)
            return redirect("profile")
        else:
            return redirect("login")
    return render(request, 'login.html')



@login_required
def logout_user(request):
    logout(request)
    return redirect('login')




@login_required
def create_task(request):
    data = request.POST
    if request.method == 'POST':
        Task.objects.create(
            name = data['name'],
            caption = data['caption']
        )
        return redirect('show_tasks')
    return render(request, 'create_tasks.html')



@login_required
def show_tasks(request):
    if request.method == 'GET':
        task = Task.objects.all()
        return render(request, 'show_tasks.html', {'task': task})



@login_required
def update_task(request, id):
    task = get_object_or_404(Task, id=id)
    data = request.POST
    if request.method == 'POST':
        task.name = data['name']
        task.caption = data['caption']
        task.save()
        return redirect('show_tasks')
    return render(request, 'update_tasks.html', {'task': task})


@login_required
def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method =='POST':
        task.delete()
        return redirect('show_tasks')
    return render(request, 'delete_tasks.html', {'task', task})