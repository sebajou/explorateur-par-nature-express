from django.urls import path, include
from UsersApp import views as user_views
from django.views.generic import TemplateView
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', user_views.wheel, name='wheel'),
    path('signup/', user_views.user_form, name='signup'),
    path('UsersApp/accounts/login/', TemplateView.as_view(template_name='registration/login.html'), name='login'),
    path('UsersApp/accounts/logout/',
         TemplateView.as_view(template_name='registration/logout.html'), name='account_logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', user_views.profile, name='profile'),
]
