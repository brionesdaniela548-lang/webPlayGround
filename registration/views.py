from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm


class LoginUserView(LoginView):
    template_name = 'registration/login.html'


class LogoutUserView(LogoutView):
    next_page = '/'


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            login(request, user)  # inicia sesión automático
            return redirect('profile')
    else:
        form = RegisterForm()

    return render(request, 'registration/signup.html', {'form': form})

@login_required
def profile_view(request):
    return render(request, 'registration/profile.html')