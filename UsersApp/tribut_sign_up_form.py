from django.contrib.auth.forms import UserCreationForm
from UsersApp.models import Tutor, Tribut, Account
from django import forms
from django.db import transaction


# noinspection PySuperArguments
class TributSignUpForm(UserCreationForm, forms.Form):
    """Form for fill sign up. """

    class Meta(UserCreationForm.Meta):
        model = Account
        fields = ('username', 'password1', 'password2', 'email')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_tribut = True
        user.save()
        tribut = Tribut.objects.create(account_tribut=user)
        return user
