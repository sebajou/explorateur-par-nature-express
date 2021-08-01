from django.shortcuts import redirect, render
from UsersApp.tribut_sign_up_form import TributSignUpForm
from UsersApp.tutor_sign_up_form import TutorSignUpForm
from UsersApp.child_sign_up_form import ChildSignUpForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as account_logout
from UsersApp.models import Tribut, Tutor, Child, Account
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from UsersApp.decorator import tribut_required
# Create your views here.


def wheel(request):
    return render(request, 'UsersApp/wheel.html')


def user_form(request):
    """Sign up form. """
    if request.method == 'POST':
        # Form for sign up from class in tribut_sign_up_form.py module
        form = TributSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # authentication and login
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        form = TributSignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def logout(request):
    if request.user.is_authenticated:
        account_logout(request)
        return render(request, 'registration/logout.html')
    else:
        return render(request, 'registration/logout.html')


@login_required
@tribut_required
def tutor_form(request):
    """Sign up form. """
    if request.method == 'POST':
        # Form for sign up from class in tribut_sign_up_form.py module
        form = TutorSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form_id_account = form.save(commit=False)
            print('id_account: ', request.user.id_account, 'form_id_account: ', form_id_account)
            form_id_account.account_tribut_id = request.user.id_account
            form_id_account.save()
            form.save_m2m()
            return redirect('wheel')
    else:
        form = TutorSignUpForm()
    return render(request, 'registration/tutor_signup.html', {'form': form})


@login_required
@tribut_required
def child_form(request):
    """Sign up form. """
    if request.method == 'POST':
        # Form for sign up from class in tribut_sign_up_form.py module
        form = ChildSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form_id_account = form.save(commit=False)
            print(request.user.id_account)
            form_id_account.account_tribut_id = request.user.id_account
            form_id_account.save()
            form.save_m2m()
            return redirect('wheel')
    else:
        form = ChildSignUpForm()
    return render(request, 'registration/child_signup.html', {'form': form})


@login_required
def profile(request):
    """Display profile page. """
    if request.user.is_authenticated:
        return render(request, 'registration/profile.html')
    else:
        return render(request, 'registration/login.html')


@login_required
@tribut_required
def tribut_profile(request):
    """Display profile page. """
    if request.user.is_authenticated:
        tutors = Tutor.objects.filter(account_tribut=request.user.id_account)
        children = Child.objects.filter(account_tribut=request.user.id_account)

        return render(request, 'UsersApp/tribut_profile.html', {'tutors': tutors, 'children': children})

    else:
        return render(request, 'registration/login.html')


@login_required
def login_success(request):
    """
    Redirects users based on whether they are in the admins group
    """
    if request.user.is_tribut:
        # user is tribut
        return redirect("tribut_profile")
    elif request.user.is_author:
        # user is author
        return redirect("author_home")
    else:
        return redirect("login")
