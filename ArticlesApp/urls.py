from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from ArticlesApp import views as article_views
from django.views.generic import TemplateView

urlpatterns = [
    path('author_home/', article_views.BibliographyView, name='author_home'),
    path('article/add/', article_views.ArticleCreateView.as_view(), name='article_create'),
    path('article/<int:pk>/<slug:slug>/', article_views.ArticleReadView.as_view(), name='article_read'),
    path('article/<int:pk>/', article_views.ArticleUpdateView.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', article_views.ArticleDeleteView.as_view(), name='article_delete'),

    path('badge/', article_views.BadgeListView.as_view(), name='badge_list'),
    path('badge/add/', article_views.BadgeCreateView.as_view(), name='badge_create'),
    path('badge/<int:pk>/<slug:slug>/', article_views.BadgeReadView.as_view(), name='badge_read'),
    path('badge/<int:pk>/', article_views.BadgeUpdateView.as_view(), name='badge_update'),
    path('badge/<int:pk>/delete/',
         article_views.BadgeDeleteView.as_view(
             template_name='ArticlesApp/badge_confirm_delete.html'),
         name='badge_confirm_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
