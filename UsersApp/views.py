from django.shortcuts import redirect, render
from UsersApp.sign_up_form import SignUpForm
from django.contrib.auth import authenticate, login
from UsersApp.models import Tribut
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


def wheel(request):
    return render(request, 'UsersApp/wheel.html')


def user_form(request):
    """Sign up form. """
    if request.method == 'POST':
        # Form for sign up from class in sign_up_form.py module
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # authentication and login
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def profile(request):
    """Display profile page. """
    if request.user.is_authenticated:
        return render(request, 'registration/profile.html')
    else:
        return render(request, 'registration/login.html')

