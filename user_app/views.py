from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.views import View
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class DashboardView(View):
    def get(self, request):
        user = request.user  # Текущий пользователь
        return render(request, 'dashboard.html', {'user': user})


class RegisterView(View):
    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Перенаправление на страницу после регистрации
        return render(request, 'register.html', {'form': form})

    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'register.html', {'form': form})


class UserLoginView(View):
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Перенаправление на страницу после входа
        return render(request, 'login.html', {'form': form})

    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
