from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from UsersApp import views as user_views
from django.views.generic import TemplateView
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', user_views.wheel, name='wheel'),
    path('signup/', user_views.user_form, name='signup'),
    path('tutor_form/', user_views.tutor_form, name='tutor_form'),
    path('child_form/', user_views.child_form, name='child_form'),
    path('UsersApp/accounts/login/', TemplateView.as_view(template_name='registration/login.html'), name='login'),
    path('UsersApp/accounts/logout/', user_views.logout, name='account_logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', user_views.profile, name='profile'),
    path('tribut_profile/', user_views.tribut_profile, name='tribut_profile'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)