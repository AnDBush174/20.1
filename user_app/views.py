# user_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    user = request.user  # Текущий пользователь
    return render(request, 'dashboard.html', {'user': user})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Перенаправление на страницу после регистрации
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Перенаправление на страницу после входа
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
