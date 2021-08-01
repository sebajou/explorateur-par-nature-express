from django.contrib.auth.forms import UserCreationForm
from UsersApp.models import Child
from django import forms
from UsersApp.models import Tribut


# noinspection PySuperArguments
class ChildSignUpForm(forms.ModelForm):
    """Form for fill sign up. """

    class Meta:
        model = Child
        exclude = ('account_tribut', )
        fields = ('child_username', 'first_name', 'last_name', 'image_profile_child')
