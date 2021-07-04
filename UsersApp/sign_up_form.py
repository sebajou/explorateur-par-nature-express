from django.contrib.auth.forms import UserCreationForm
from UsersApp.models import Users, Tribut
from django import forms


class SignUpForm(UserCreationForm, forms.Form):
    """Form for fill sign up. """

    # Tribut from many to many field. Only one choice possible.
    tribut_name = forms.CharField(queryset=Tribut.objects.all())

    class Meta:
        model = Users
        fields = ('username', 'tribut_name', 'password1', 'password2', 'first_name', 'last_name', 'email', 'image_profile')
