from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from ArticlesApp import views as article_views
from django.views.generic import TemplateView

urlpatterns = [
    path('author_home/', article_views.author_home, name='author_home'),
    path('article_create/', article_views.article_create, name='article_create'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
