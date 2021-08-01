from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as account_logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from ArticlesApp.decorator import author_required
from ArticlesApp.models import Author, Article
# Create your views here.


@login_required
@author_required
def author_home(request):
    """Display home page for authors with author s articles. """
    if request.user.is_authenticated:
        author = Author.objects.filter(account_author=request.user.id_account)

        return render(request, 'author_home.html', {'author': author})

    else:
        return render(request, 'registration/login.html')


@login_required
@author_required
def article_create(request):
    pass
