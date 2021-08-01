from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as account_logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from ArticlesApp.decorator import author_required
from ArticlesApp.models import Bibliography, Author, Article
# Create your views here.


@login_required
@author_required
def author_home(request):
    """Display home page for authors with author s articles. """
    if request.user.is_authenticated:
        bibliography = Bibliography.objects.filter(account_author=request.user.account_author)
        article = Article.objects.filter(id_article=bibliography.id_article)

        return render(request, 'author_home.html', {'article': article})

    else:
        return render(request, 'registration/login.html')


@login_required
@author_required
def article_create(request):
    pass
