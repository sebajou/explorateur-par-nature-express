from django.shortcuts import redirect, render
from UsersApp.tribut_sign_up_form import TributSignUpForm
from UsersApp.tutor_sign_up_form import TutorSignUpForm
from UsersApp.child_sign_up_form import ChildSignUpForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as account_logout
from UsersApp.models import Tribut, Tutor, Child, Account, Badge
from ArticlesApp.models import Article, Image
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from UsersApp.decorator import tribut_required
# Create your views here.
from django.test import TransactionTestCase


def wheel(request):
    articles = Article.objects.all()

    return render(request, 'UsersApp/wheel.html', {'articles': articles})


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
    """Log out"""
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
    Redirects users based on whether they are in the admins groupli
    """
    if request.user.is_tribut:
        # user is tribut
        return redirect("tribut_profile")
    elif request.user.is_author:
        # user is author
        return redirect("author_home")
    else:
        return redirect("login")


@login_required
@tribut_required
def articles_child_success(request):
    """Attribute a success to an article for a child. """
    if request.method == 'POST':
        id_childs = request.POST.getlist('id_child')
        print('id_chils', id_childs)
        for id_child in id_childs:
            id_article = request.POST.get('id_article')
            instance_child = Child.objects.get(id_child=id_child)
            instance_article = Article.objects.get(id_article=id_article)
            instance_article.success_article.add(instance_child)
    return redirect('wheel')


@login_required
@tribut_required
def article_child_success_choice(request):
    """Page for choose the child which succeed with the previous read article"""
    if request.method == 'POST':
        id_article = request.POST.get('id_article')
        article = Article.objects.filter(id_article=id_article)
        print('id_article ', id_article)
        q_child = Child.objects.filter(account_tribut=request.user.id_account).values()
        print('q_child ', q_child)
        return render(request, 'UsersApp/article_success_child_choice.html',
                      {'q_child': q_child, 'id_article': id_article, 'article': article})


@login_required
@tribut_required
def gallery_of_child_trophies(request, id_child):
    """ Fill the trophies table (where are record the badges win for each child) et display it """
    if request.method == 'POST':
        id_child = request.POST.get('id_child')

        # Give badges to the child if the badge's articles are all success
        all_id_badges = Badge.objects.values_list('id_badge', flat=True)
        all_true = False
        for id_badge in all_id_badges:
            articles_of_child = Article.objects.filter(success_article=id_child, id_badge=id_badge).values('id_article')
            articles_of_badge = Article.objects.filter(id_badge=id_badge).values('id_article')
            if (list(articles_of_badge)) == (list(articles_of_child)):
                all_true = True
            else:
                all_true = False
            if all_true:
                instance_child = Child.objects.get(id_child=id_child)
                instance_badge = Badge.objects.get(id_badge=id_badge)
                instance_child.trophies.add(instance_badge)
                all_true = False

        # List the badge win by the child
        child = Child.objects.filter(id_child=id_child)
        child_trophies = Badge.objects.filter(child__id_child=id_child)

        return render(request, 'UsersApp/gallery_of_child_trophies.html',
                      {'child_trophies': child_trophies, 'child': child})
