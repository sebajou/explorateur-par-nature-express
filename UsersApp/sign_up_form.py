from django.contrib.auth.forms import UserCreationForm
from UsersApp.models import Tutor, Tribut
from django import forms


# noinspection PySuperArguments
class SignUpForm(UserCreationForm, forms.Form):
    """Form for fill sign up. """

    class Meta:
        model = Tribut
        fields = ('username', 'password1', 'password2', 'email')

    # def save(self, commit=True):
    #     user = super(UserCreationForm, self).save(commit=False)
    #     user.first_name = user.username
    #     user.last_name = user.username
    #     user.save()
    #     return user
